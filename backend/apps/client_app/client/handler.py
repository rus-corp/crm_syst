from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi import status

from apps.program_rooms_app.dals import ProgramRoomDAL

from ...base.base_handler import BaseHandler
from .dals import ClientDAL
from .. import schemas
from ...utils.slug import create_slug
from ..mixin import ClientMixin
from apps.base.exceptions import AppBaseExceptions
from core.models.client_models import ClientProfile, ClientDocument
from .utils import check_sharing, check_free_room_volume
from ...payments_app.handlers import PaymentHandler



class ClientHandler(ClientMixin, BaseHandler):
  def __init__(self, session):
    super().__init__(session)
  
  async def _create_client(self, client_body: schemas.CreateClient):
    async with self.session.begin():
      body_data = client_body.model_dump(exclude_none=True)
      client_slug = await self.check_and_create_client_slug(body_data)
      body_data['slug'] = client_slug
      created_client = await self.client_dal.create_client(**body_data)
      return created_client
  
  
  async def _get_clients_list(self):
    clients = await self.client_dal.get_clients()
    return list(clients)
  
  
  async def _get_client_by_id(self, client_id: int):
    client = await self.client_dal.get_client_by_id(client_id)
    return client
  
  
  async def _get_client_by_slug(self, client_slug: str):
    client = await self.client_dal.get_client_by_slug(client_slug)
    return client
  
  
  async def _get_client_current_program(self, client_slug: str, flag: bool = False):
    if not flag:
      client_program = await self.client_dal.get_client_current_program(client_slug)
    else:
      client_program = await self.client_dal.get_client_current_program_with_profile_and_doc(client_slug)
    if client_program is None:
      return JSONResponse(
        status_code=200,
        content='Client does not have a current program'
      )
    return client_program
  
  
  async def _get_client_with_profile_and_doc(self, client_slug: str, flag: bool = False):
    if flag:
      client = await self.client_dal.get_get_client_profile_and_doc_with_family(client_slug)
    else:
      client = await self.client_dal.get_client_profile_and_doc(client_slug)
      # client_profile = 
      # client_doc = 
      if client is None:
        return AppBaseExceptions.item_not_found(item_data='Client')
    return client
  
  
  async def _update_client(self, client_id: int, client_data: schemas.UpdateClientRequest):
    async with self.session.begin():
      body_data = client_data.model_dump(exclude_none=True)
      updated_client = await self.client_dal.update_client_by_id(
        client_id=client_id,
        values=body_data
      )
      if updated_client is None:
        return AppBaseExceptions.item_not_found('Client')
      return updated_client
  
  
  async def _create_client_with_profile(self, client_data: schemas.CreateClientWithProfileRequest):
    async with self.session.begin():
      body_data = client_data.model_dump(exclude_none=True)
      profile_data = body_data.pop('profile')
      if not profile_data:
        return AppBaseExceptions.need_data(item_data='Profile')
      client_slug = await self.check_and_create_client_slug(body_data)
      body_data['slug'] = client_slug
      client: schemas.BaseShowClient = await self.client_dal.get_or_create_client(values=body_data)
      if client is None:
        return AppBaseExceptions.item_create_error(item_data='Client')
      profile_data['client_id'] = client.id
      client_profile = await self.client_dal.base_create_item(
        model=ClientProfile,
        values=profile_data,
        commit=True
      )
      if client_profile is None:
        return AppBaseExceptions.item_create_error(item_data='Profile')
      return schemas.ClientProfileCreateResponse(
        id=client.id,
        last_name=client.last_name,
        name=client.name,
        second_name=client.second_name,
        phone=client.phone,
        email=client.email,
        created_at=client.created_at,
        updated_at=client.updated_at,
        slug=client.slug,
        profile=client_profile
      )
  
  
  async def _create_client_profile_doc(self, client_data: schemas.CreateClientWithProfileAndDocRequest):
    async with self.session.begin():
      body_data = client_data.model_dump(exclude_none=True)
      profile_data = body_data.pop('profile')
      doc_data = body_data.pop('doc')
      if not profile_data or not doc_data:
        return AppBaseExceptions.need_data(item_data='Profile or Document')
      client_slug = await self.check_and_create_client_slug(body_data)
      body_data['slug'] = client_slug
      client: schemas.BaseShowClient = await self.client_dal.get_or_create_client(body_data)
      if client is None:
        return AppBaseExceptions.item_create_error('Client')
      profile_data['client_id'] = client.id
      doc_data['client_id'] = client.id
      client_profile = await self.client_dal.base_create_item(
        model=ClientProfile,
        values=profile_data
      )
      if client_profile is None:
        return AppBaseExceptions.item_create_error(item_data='Profile')
      client_doc = await self.client_dal.base_create_item(
        model=ClientDocument,
        values=doc_data,
        commit=True
      )
      if client_doc is None:
        return AppBaseExceptions.item_create_error(item_data='Profile')
      return schemas.ClientProfileDocCreateResponse(
        id=client.id,
        last_name=client.last_name,
        name=client.name,
        second_name=client.second_name,
        phone=client.phone,
        email=client.email,
        created_at=client.created_at,
        updated_at=client.updated_at,
        slug=client.slug,
        profile=client_profile,
        document=client_doc
      )
  
  
  async def _append_client_to_program_room(self, body: schemas.AppendClientToProgramRoom):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      program_room_dal = ProgramRoomDAL(self.session)
      program_room_clients = await program_room_dal.get_program_room_client(body_data['program_room_id'])
      sharing = check_sharing(program_room_clients)
      if sharing:
        raise AppBaseExceptions.closed_setlement()
      free_room_vol = check_free_room_volume(program_room_clients)
      if free_room_vol == 0:
        raise AppBaseExceptions.closed_setlement()
      try:
        append_client_to_room = await program_room_dal.append_client_to_program_room(**body_data)
        client_program_price = await self.save_program_price(body_data['program_client_id'])
        return JSONResponse(status_code=status.HTTP_201_CREATED, content='Клиент заселен, цена поездки сохранена')
      except Exception as e:
        await self.session.rollback()
        raise AppBaseExceptions.item_create_error(
          item_data='Client Program Room',
          exception_message=f'Не удалось заселить клиента {e}'
        )
      
      
      
      # room_volume = program_room.room.room_volume
      # check_program_client_room = await self.client_dal.
      """
      1. проверить наличие места в комнате
      2. заселить клиента
      3. посчитать и записать стоимость поездки клиента в ProgramClients
      """
      # check_value_program_room = 
      # client_program_room = await self.client_dal.append_client_to_room(**body_data)
      