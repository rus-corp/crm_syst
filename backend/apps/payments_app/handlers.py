from fastapi.exceptions import HTTPException
from fastapi import status
from .dals import PaymentDAL

from ..base.base_handler import BaseHandler
from . import schemas
from core.models.utils import ClientProgramStatus





class PaymentHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.payment_dal = PaymentDAL(self.session)
  
  
  async def _create_client_payment(self, payment_body: schemas.CreateClientPaymentBody):
    async with self.session.begin():
      body_data = payment_body.model_dump()
      current_client_program = await self.payment_dal.get_current_client_program(
        client_id=body_data['client_id'],
        program_id=body_data['program_id']
      )
      if current_client_program is None:
        raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail='Current Client Program not found'
        )
      client_payment = await self.payment_dal.create_payment(
        client_program_id=current_client_program.id,
        amount=body_data['amount']
      )
      if client_payment:
        client_payments = await self.payment_dal.get_client_program_payments(current_client_program.id)
        paid_amount = 0
        for payment in client_payments:
          paid_amount += payment.amount
        if paid_amount < current_client_program.price:
          await self.payment_dal.update_program_client_status(current_client_program.id, status=ClientProgramStatus.AC)
        elif paid_amount >= current_client_program.price:
          await self.payment_dal.update_program_client_status(current_client_program.id, status=ClientProgramStatus.PF)
        return client_payment
  
  
  async def _get_client_program_payments(self, program_client_id: int):
    client_program_payments = await self.payment_dal.get_client_program_payments(program_client_id)
    return client_program_payments
  
  
  async def _update_client_program_price(self, program_client_id: int, amount: int):
    values = {'price': amount}
    update_price = await self.payment_dal.update_program_clients_table(
      program_clients_id=program_client_id,
      values=values
    )
    return update_price