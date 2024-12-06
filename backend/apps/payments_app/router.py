from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.database import get_db
from . import schemas
from .handlers import PaymentHandler
from . import schemas




router = APIRouter(
  prefix='/payments',
  tags=['Payments']
)



@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ClientPaymentsResponse
)
async def create_client_program_payment(
  body: schemas.CreateClientPaymentBody,
  session: AsyncSession = Depends(get_db)
):
  payment_handler = PaymentHandler(session)
  created_payment = await payment_handler._create_client_payment(body)
  return created_payment



@router.get(
  '/{program_client_id}',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.ClientPaymentsResponse]
)
async def get_client_program_payments(
  program_client_id: int,
  session: AsyncSession = Depends(get_db)
):
  payment_handler = PaymentHandler(session)
  client_program_payments = await payment_handler._get_client_program_payments(program_client_id)
  return client_program_payments