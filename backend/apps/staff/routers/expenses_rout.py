from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .. import schemas
from core.database import get_db
from ..handlers.expense_handler import ExpenseHandler
from apps.base.base_schemas import BaseMessageResponseModel


router = APIRouter(
  
)




@router.post(
  '/expenses',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ExpenseBaseResponse
)
async def crete_expenses(
  body: schemas.ExpenseCreateRequst,
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  created_item = await expenses_handler._create_expenses(body)
  return created_item



@router.get(
  '/expenses/{expense_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ExpenseBaseResponse
)
async def get_expenses_by_id(
  expense_id: int,
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  expense = await expenses_handler._get_expense_by_id(expense_id)
  return expense


@router.post(
  '/append_expense',
  status_code=status.HTTP_200_OK,
  response_model=BaseMessageResponseModel
)
async def append_expenses_to_program(
  body: schemas.AppendExpensesToProgram,
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  created_item = await expenses_handler._append_expensive_to_program(
    body
  )
  return created_item


