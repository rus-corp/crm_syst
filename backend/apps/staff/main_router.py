from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from .handlers import EmployeeHandler, ExpenseHandler
from . import schemas
from apps.base.base_schemas import BaseMessageResponseModel


router = APIRouter(
  prefix='/staff',
  tags=['Staff']
)









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


@router.post(
  '/employee_expenses',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.CreateEmployeeWithExpensesResponse
)
async def create_employee_and_expenses(
  body: schemas.CreateEmployeeWithExpensesRequest,
  session: AsyncSession = Depends(get_db)
):
  employee_handler = EmployeeHandler(session)
  created_data = await employee_handler._create_employee_and_expenses(body)
  return created_data