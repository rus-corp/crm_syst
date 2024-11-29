from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.database import get_db
from . import schemas
from .handlers import PaymentHandler




router = APIRouter(
  prefix='/payments',
  tags=['Payments']
)



@router.post(
  '/',
  status_code=status.HTTP_201_CREATED
)
async def create_client_program_payment(
  body: schemas.CreateClientPaymentBody,
  session: AsyncSession = Depends(get_db)
):
  payment_handler = PaymentHandler(session)
  created_payment = await payment_handler._create_client_payment(body)
  return created_payment