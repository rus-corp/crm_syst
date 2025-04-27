from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import selectinload, joinedload



from ...base.base_dal import BaseDAL
from datetime import date


from core.models.program_models import Program
from core.models.staff_models import Expenses
from core.models.partners_models import ProgramPartners, PartnerService
from core.models.association_models import ProgramClients, ProgramRooms, ProgramPartners
from core.models.utils import ProgramStatus



class ProgramDAL(BaseDAL):
  model = Program
  
  async def create_program(
    self,
    title: str,
    start_date: date,
    end_date: date,
    place: str,
    desc: str,
    slug: str,
    client_count: int,
  ):
    new_program: Program = Program(
      title=title,
      start_date=start_date,
      end_date=end_date,
      place=place,
      desc=desc,
      slug=slug,
      client_count=client_count
    )
    self.db_session.add(new_program)
    await self.db_session.commit()
    return new_program
  
  
  async def get_all_programs(self):
    return await self.base_get_all_items(model=self.model)
  
  
  async def get_active_programs(self):
    query = select(Program).order_by(Program.id).filter(Program.status == ProgramStatus.AC)
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def get_program_by_id(self, program_id: int):
    result = await self.base_get_one_item(
      model=self.model,
      item_id=program_id
    )
    return result
  
  
  async def get_program_by_slug(self, program_slug: str):
    result = await self.base_get_one_item_by_slug(
      model=self.model,
      item_slug=program_slug
    )
    return result
  
  
  async def get_program_by_id_with_clients(self, program_id: int):
    query = (select(Program)
             .options(
               selectinload(Program.program_clients_detail)
               .joinedload(ProgramClients.client)
             )
             .filter(Program.id == program_id))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_program_clients_with_payments(self, program_id: int):
    query = (select(ProgramClients)
             .where(ProgramClients.program_id == program_id)
             .options(
               joinedload(ProgramClients.client),
               joinedload(ProgramClients.client_program_payments)
             ))
    result = await self.db_session.execute(query)
    return result.scalars().unique().all()
  
  
  async def update_program_by_slug(self, program_slug: str, values):
    stmt = (update(Program)
            .where(Program.slug == program_slug)
            .values(**values)
            .returning(Program))
    result = await self.db_session.execute(stmt)
    return result.scalar()
  
  
  async def check_program_client(self, program_id: int, client_id: int):
    query = (select(ProgramClients)
             .filter(
               ProgramClients.program_id == program_id,
               ProgramClients.client_id == client_id
             ))
    result = await self.db_session.scalar(query)
    return result or None
  
  
  async def get_client_active_program(self, client_id: int):
    query = select(ProgramClients).options(joinedload(ProgramClients.program)).filter(ProgramClients.client_id == client_id, Program.status == 'AC')
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def change_client_program(self, program_client_id: int, updated_values: dict):
    # stmt = update(ProgramClients).filter(ProgramClients.program_id == program_id, ProgramClients.client_id == client_id).values(**updated_values).returning(ProgramClients)
    stmt = update(ProgramClients).where(ProgramClients.id == program_client_id).values(**updated_values).returning(ProgramClients)
    result = await self.db_session.execute(stmt)
    return result.scalar()
  
  
  
  async def delete_client_from_program(
    self,
    program_id: int,
    client_id: int
  ):
    stmt = (delete(ProgramClients)
            .where(
              ProgramClients.program_id == program_id,
              ProgramClients.client_id == client_id
            )).returning(ProgramClients.id)
    result = await self.db_session.execute(stmt)
    await self.db_session.commit()
    return result.scalar()
  
  
  async def get_program_hotels(self, program_id: int):
    query = (select(ProgramRooms)
             .where(ProgramRooms.program_id == program_id)
             .options(
               joinedload(ProgramRooms.hotel),
               joinedload(ProgramRooms.room)
             ))
    result = await self.db_session.execute(query)
    return result.scalars().unique().all()
  
  
  async def get_program_for_append_expenses(self, program_id: int):
    query = (select(Program)
             .where(Program.id == program_id)
             .options(selectinload(Program.expenses)))
    return await self.db_session.scalar(query)
  
  
  async def get_program_expenses(self, program_id: int):
    query = (select(Program)
             .where(Program.id == program_id)
             .options(selectinload(Program.expenses).joinedload(Expenses.employee)))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_program_prices(self, program_id: int):
    query = (select(Program)
             .where(Program.id == program_id)
             .options(selectinload(Program.prices)))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_program_partners(self, program_id: int):
    query = (select(ProgramPartners)
             .where(ProgramPartners.program_id == program_id)
             .options(
               joinedload(ProgramPartners.partner),
               joinedload(ProgramPartners.service),
             ))
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def get_program_by_id_with_expenses_and_partners(self, program_id: int):
    query = (select(Program)
             .where(Program.id == program_id)
             .options(
               selectinload(Program.expenses),
               selectinload(Program.program_partner).joinedload(ProgramPartners.service)
             ))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_program_hotel_rooms(self, program_room_id: int):
    query = select(ProgramRooms).where(ProgramRooms.id == program_room_id).options(joinedload(ProgramRooms.room))
    result = await self.db_session.execute(query)
    return result.scalar()