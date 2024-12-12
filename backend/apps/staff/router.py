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
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.EmployeeResponse
)
async def create_employee(
  body: schemas.CreateEmployeeRequest,
  session: AsyncSession = Depends(get_db)
):
  employee_handler = EmployeeHandler(session)
  created_item = await employee_handler._create_employee(body)
  return created_item



@router.get(
  '/',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.EmployeeResponse]
)
async def get_all_employee(
  session: AsyncSession = Depends(get_db)
):
  employee_handler = EmployeeHandler(session)
  employeers_list = await employee_handler._get_all_employees()
  return employeers_list


@router.get(
  '/{employee_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.EmployeeResponse
)
async def get_employee(
  employee_id: int,
  session: AsyncSession = Depends(get_db)
):
  employee_handler = EmployeeHandler(session)
  employeer = await employee_handler._get_employee(employee_id)
  return employeer



@router.patch(
  '/{employee_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.EmployeeResponse
)
async def update_employee(
  employee_id: int,
  body: schemas.EmployeeUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  employee_handler = EmployeeHandler(session)
  employeer = await employee_handler._update_employee(
    employee_id=employee_id,
    body=body
  )
  return employeer



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