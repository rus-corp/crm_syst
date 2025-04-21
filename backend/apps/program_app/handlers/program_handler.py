from fastapi.responses import JSONResponse


from ...utils.slug import create_slug
from ...base.base_handler import BaseHandler
from .. import schemas
from core.models.program_models import Program
from core.models.association_models import ProgramClients
from ...client_app.client.dals import ClientDAL
from ..utils import data_format, program_response_format, calculate_program_expenses, calculate_program_partners
from apps.hotels_app.hotels.schemas import HotelWithRooms, ProgramHotelRoomsResponse
from apps.hotels_app.hotels.utils import get_hotel_rooms_volume
from apps.base.exceptions import AppBaseExceptions
from apps.staff.schemas import AppendExpensesToProgram
from apps.staff.dals.expenses_dal import ExpensesDAL
from ..mixin import ProgramMixin
from .program_base_handler import ProgramBaseHandler
from ..dals.prog_price_dal import ProgramPriceDAL



class ProgramHandler(ProgramMixin, ProgramBaseHandler):
  
  async def _get_program_clients(self, program_id: int):
    async with self.session.begin():
      program_clients = await self.program_dal.get_program_by_id_with_clients(program_id)
      clients = program_clients.program_clients_detail
      duration = program_clients.duration()
      return schemas.ProgramClientsResponse(
        id=program_clients.id,
        title=program_clients.title,
        start_date=program_clients.start_date,
        end_date=program_clients.end_date,
        place=program_clients.place,
        desc=program_clients.desc,
        slug=program_clients.slug,
        status=program_clients.status,
        duration=duration,
        program_clients_detail=program_clients.program_clients_detail
      )
  
  
  async def _append_client_to_program(
    self,
    body: schemas.AppendClientToProgramRequest
  ):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      client_program = await self.check_current_client_program(body_data['client_id'])
      if client_program is None:
        current_program: Program = await self.program_dal.get_program_by_id_with_clients(program_id=body_data['program_id'])
        client_dal = ClientDAL(self.session)
        current_client = await client_dal.get_client_by_id(body_data['client_id'])
        current_program.program_clients_detail.append(
          ProgramClients(
            client=current_client,
            program=current_program,
          )
        )
        await self.session.commit()
        return JSONResponse('Клиент добавлен', status_code=201)
      else:
        updated_program = await self.program_dal.change_client_program(
          program_client_id=client_program.id,
          updated_values=body_data
        )
        return JSONResponse('Программа клиента изменена', status_code=201)
  
  
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
          ProgramHotelRoomsResponse(
            id=key,
            program_room_id=value['program_room_id'],
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
  
  
  async def _get_program_expenses(self, program_id: int):
    program = await self.program_dal.get_program_expenses(program_id)
    return program
  
  
  async def _append_expensive_to_program(self, body: AppendExpensesToProgram):
    async with self.session.begin():
      program, expensive_item = await self.check_program_and_expenses(body)
      program.expenses.append(expensive_item)
      return JSONResponse(content=f'Expenses added to Program {program.title}', status_code=201)
  
  
  async def _delete_expensive_from_program(self, body: AppendExpensesToProgram):
    async with self.session.begin():
      program, expensive_item = await self.check_program_and_expenses(body)
      if expensive_item not in program.expenses:
        raise AppBaseExceptions.relation_not_exsist(
          main_model='Program',
          main_item_id=body.program_id,
          second_model='Expenses',
          second_item_id=body.expenses_id
        )
      program.expenses.remove(expensive_item)
      return JSONResponse(content='Expenses deleted from Program', status_code=200)
  
  
  async def _calculate_program_prices(self, program_id: int):
    """
    Получаем программу -> 
    получаем статические затраты, затраты на аерсонал, затраты на партнеров -> 
    считаем цену и пишем в базу
    """
    async with self.session.begin():
      program = await self.program_dal.get_program_by_id_with_expenses_and_partners(program_id)
      if program is None:
        raise AppBaseExceptions.item_not_found('Program')
      program_total_expenses = calculate_program_expenses(program.expenses, program.client_count)
      program_total_partners = calculate_program_partners(program.program_partner, program.client_count)
      program_prices_dal = ProgramPriceDAL(self.session)
      program_prices = {
        'base_price': program_total_expenses + program_total_partners,
        'loayal_price': (program_total_expenses + program_total_partners) - 2000,
        'comunity_price': (program_total_expenses + program_total_partners) - 5000,
        'program_id': program.id
      }
      create_program_prices = await program_prices_dal.create_program_price(program_prices)
      return create_program_prices
  
  
  async def _get_program_partners(self, program_id: int):
      program_partners = await self.program_dal.get_program_partners(program_id)
      return list(program_partners)