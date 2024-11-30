

from ..base.base_handler import BaseHandler
from .dals import ClientDAL
from . import schemas
from ..utils.slug import create_slug


class ClientHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.client_dal = ClientDAL(self.session)
  
  
  async def _create_client(self, client_body: schemas.CreateClient):
    async with self.session.begin():
      body_data = client_body.model_dump(exclude_none=True)
      client_slug = create_slug(body_data['name'] + body_data['last_name'])
      body_data['slug'] = client_slug
      created_client = await self.client_dal.create_client(**body_data)
      return created_client
  
  
  async def _get_clients_list(self):
    async with self.session.begin():
      clients = await self.client_dal.get_clients()
      return list(clients)
  
  
  async def _get_client_by_id(self, client_id: int):
    async with self.session.begin():
      client = await self.client_dal.get_client_by_id(client_id)
      return client
  
  
  async def _get_client_by_slug(self, client_slug: str):
    async with self.session.begin():
      client = await self.client_dal.get_client_by_slug(client_slug)
      return client
  
  
  async def _get_client_current_program(self, client_slug: str):
    async with self.session.begin():
      client_program = await self.client_dal.get_client_current_program(client_slug)
      return client_program
  
  
  async def _update_client(self, client_id: int, client_data):pass