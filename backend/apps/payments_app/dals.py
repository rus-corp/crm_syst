from sqlalchemy import select, update
from sqlalchemy.orm import selectinload, joinedload

from core.models.program_models import Program
from ..base.base_dal import BaseDAL
from core.models.association_models import ProgramClients
from core.models.payment_models import ClientProgramPayment





class PaymentDAL(BaseDAL):
  async def create_payment(self, client_program_id: int, amount: int):
    new_payment: ClientProgramPayment = ClientProgramPayment(
      client_program_id=client_program_id,
      amount=amount
    )
    self.db_session.add(new_payment)
    await self.db_session.flush()
    return new_payment
  
  
  async def get_current_client_program(
    self,
    client_id: int,
    program_id: int
  ):
    query = (select(ProgramClients)
             .filter(
               ProgramClients.program_id == program_id,
               ProgramClients.client_id == client_id
             ))
    result = await self.db_session.scalar(query)
    return result
  
  
  async def update_program_client_status(self, client_program_id: int, status: str):
    query = update(ProgramClients).where(ProgramClients.id == client_program_id).values(status=status)
    await self.db_session.execute(query)
  
  
  
  async def get_client_program_payments(self, program_client_id: int):
    query = select(ClientProgramPayment).where(ClientProgramPayment.client_program_id == program_client_id)
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def update_program_clients_table(self, program_clients_id: int, values: dict):
    result = await self.base_update_item(
      model=ProgramClients,
      item_id=program_clients_id,
      values=values
    )
    await self.db_session.flush()
    return result
  
  
  async def get_client_program_price(self, program_client_id: int):
    query = select(ProgramClients).where(ProgramClients.id == program_client_id).options(joinedload(ProgramClients.program).joinedload(Program.prices))
    return await self.db_session.scalar(query)