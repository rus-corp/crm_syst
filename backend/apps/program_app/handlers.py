from fastapi.responses import JSONResponse


from ..utils.slug import create_slug
from ..base.base_handler import BaseHandler
from .dals import ProgramDAL
from . import schemas
from core.models.program_models import Program
from core.models.association_models import ProgramClients
from ..client_app.client.dals import ClientDAL
from .utils import data_format
from apps.hotels_app.hotels.schemas import HotelWithRooms
from apps.hotels_app.hotels.utils import get_hotel_rooms_volume




class ProgramHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.program_dal = ProgramDAL(self.session)
  
  
  
  async def _create_program(
    self,
    create_program_body: schemas.CreateProgramRequets
  ) -> schemas.ProgramBaseResponse:
    async with self.session.begin():
      body_data = create_program_body.model_dump(exclude_none=True)
      slug = create_slug(body_data['title'] + str(body_data['start_date']))
      check_program = await self.program_dal.get_program_by_slug(slug)
      if check_program:
        slug += body_data['end_date']
      body_data['slug'] = slug
      created_program = await self.program_dal.create_program(**body_data)
      return schemas.ProgramBaseResponse(
        id=created_program.id,
        title=created_program.title,
        start_date=created_program.start_date,
        end_date=created_program.end_date,
        place=created_program.place,
        status=created_program.status,
        price=created_program.price,
        desc=created_program.desc,
        slug=created_program.slug
      )
  
  
  async def _get_programs_list(self):
    programs_list = await self.program_dal.get_active_programs()
    programs = []
    for program in programs_list: # type Program
      duration = program.duration()
      programs.append(
        schemas.ProgramBaseResponse(
          id=program.id,
          title=program.title,
          start_date=program.start_date,
          end_date=program.end_date,
          place=program.place,
          status=program.status,
          price=program.price,
          desc=program.desc,
          slug=program.slug,
          duration=duration
        )
      )
    return programs
  
  
  async def _get_program_by_slug(
    self,
    program_slug: str
  ):
    program = await self.program_dal.get_program_by_slug(program_slug)
    return program
  
  
  
  async def _get_program_clients(self, program_id: int):
    async with self.session.begin():
      program_clients = await self.program_dal.get_program_by_id_with_clients(program_id)
      return program_clients
  
  
  
  async def _append_client_to_program(
    self,
    body: schemas.AppendClientToProgramRequest
  ):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      current_program: Program = await self.program_dal.get_program_by_id_with_clients(program_id=body_data['program_id'])
      client_dal = ClientDAL(self.session)
      current_client = await client_dal.get_client_by_id(body_data['client_id'])
      current_program.program_clients_detail.append(
        ProgramClients(
          client=current_client,
          program=current_program,
          price=body_data.get('price')
        )
      )
      await self.session.commit()
      return JSONResponse('клиент добавлен', status_code=201)
  
  
  async def _delete_client_from_program(
    self,
    body: schemas.DeleteClientFromProgramRequest
  ):
    async with self.session.begin():
      body_data = body.model_dump()
      check_relation = self.program_dal.check_program_client(
        program_id=body_data['program_id'],
        client_id=body_data['client_id']
      )
      if check_relation:
        deleted_client = self.program_dal.delete_client_from_program(
          program_id=body_data['program_id'],
          client_id=body_data['client_id']
        )
        return deleted_client
  
  
  
  async def _get_program_clients_with_payments(self, program_id: int):
    async with self.session.begin():
      program_clients = await self.program_dal.get_program_clients_with_payments(program_id)
      return program_clients
  
  
  async def get_program_hotels(self, program_id: int):
    async with self.session.begin():
      program_hotels = await self.program_dal.get_program_hotels(program_id)
      response_data = data_format(program_hotels)
      response_list = []
      for key, value in response_data.items():
        rooms_volume = get_hotel_rooms_volume(value['rooms'])
        response_list.append(
          HotelWithRooms(
            id=key,
            title=value['title'],
            address=value['address'],
            contacts=value['contacts'],
            email=value['email'],
            desc=value['desc'],
            city=value['city'],
            rooms=value['rooms'],
            hotel_rooms_volume=rooms_volume
          )
        )
      return response_list