from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .. import schemas
from core.database import get_db
from ..handlers.expense_handler import ExpenseHandler
from apps.base.base_schemas import BaseMessageResponseModel


router = APIRouter(
  prefix='/expenses',
  tags=['Expenses']
)




@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ExpenseBaseResponse
)
async def create_expenses(
  body: schemas.ExpenseCreateRequst,
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  created_item = await expenses_handler._create_expenses(body)
  return created_item



@router.get(
  '/',
  status_code=status.HTTP_200_OK,
  # response_model=list[schemas.ExpenseBaseResponse]
)
async def get_all_expenses(
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  expenses = await expenses_handler._get_all_expenses()
  return expenses



@router.get(
  '/{expense_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ExpenseFullResponse
)
async def get_expenses_by_id(
  expense_id: int,
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  expense = await expenses_handler._get_expense_by_id(expense_id)
  return expense


@router.patch(
  '/{expense_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ExpenseBaseResponse
)
async def update_expense(
  expense_id: int,
  body: schemas.ExpensesUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  updated_expense = await expenses_handler._update_expense_by_id(
    expense_id, body=body
  )
  return updated_expense



@router.delete(
  '/{expense_id}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def delete_expense_by_id(
  expense_id: int,
  session: AsyncSession = Depends(get_db)
):
  expenses_handler = ExpenseHandler(session)
  deleted_expense = await expenses_handler._delete_expense_by_id(expense_id)
  return deleted_expense




@router.post(
  '/category_expense',
  status_code=status.HTTP_201_CREATED
)
async def create_expense_with_category(
  session: AsyncSession = Depends(get_db)
):
  expense_handler = ExpenseHandler(session)
  created_expense = await expense_handler
  return created_expense