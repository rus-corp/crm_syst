from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import selectinload, joinedload



from ..base.base_dal import BaseDAL
from datetime import date


from core.models.program_models import Program
from core.models.association_models import ProgramClients, ProgramRooms
from core.models.utils import ProgramStatus



class ProgramDAL(BaseDAL):
  async def create_program(
    self,
    title: str,
    start_date: date,
    end_date: date,
    place: str,
    desc: str,
    price: int,
    slug: str,
  ):
    new_program: Program = Program(
      title=title,
      start_date=start_date,
      end_date=end_date,
      place=place,
      desc=desc,
      price=price,
      slug=slug,
    )
    self.db_session.add(new_program)
    await self.db_session.commit()
    return new_program
  
  
  async def get_all_programs(self):
    return await self.base_get_all_items(Program)
  
  
  async def get_active_programs(self):
    query = select(Program).order_by(Program.id).filter(Program.status == ProgramStatus.AC)
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def get_program_by_id(self, program_id: int):
    query = select(Program).where(Program.id == program_id)
    return await self.db_session.scalar(query)
  
  
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
  
  
  async def update_program_by_id(self, program_id: int, **values):
    stmt = update(Program).where(Program.id == program_id).values(values).returning(Program)
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
    # query = select(Program).where(Program.id == program_id).options(selectinload(Program.program_hotel_room).joinedload(ProgramRooms.hotel), joinedload(ProgramRooms.room))
    query = select(ProgramRooms).where(ProgramRooms.program_id == program_id).options(joinedload(ProgramRooms.hotel), joinedload(ProgramRooms.room))
    result = await self.db_session.execute(query)
    # return result.scalar()
    return result.scalars().unique().all()