from typing import Dict, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from .. import schemas
from ..handlers.employee_handler import EmployeeHandler
from .utils import employee_position_variants, positions_list

router = APIRouter(
  prefix='/employee',
  tags=['Employee']
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
  response_model=schemas.EmployeeResponse,
  description=employee_position_variants
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


@router.delete(
  '/{employee_id}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def delete_employee_by_id(
  employee_id: int,
  session: AsyncSession = Depends(get_db)
):
  employee_handler = EmployeeHandler(session)
  deleted_employeer = await employee_handler._delete_employee(employee_id)
  return deleted_employeer
  



@router.post(
  '/employee_expenses/',
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



@router.get(
  '/employee_expenses/',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.EmployeeWithExpenseData]
)
async def get_all_employee_with_expenses(
  session: AsyncSession = Depends(get_db),
  limit: bool = False
):
  employee_handler = EmployeeHandler(session)
  if limit:
    employeer_list = await employee_handler._get_all_employees_with_expenses(empl_limit=8)
  else:
    employeer_list = await employee_handler._get_all_employees_with_expenses()
  return employeer_list



@router.get(
  '/employee_expenses/{employeer_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.CreateEmployeeWithExpensesResponse
)
async def get_employeer_with_expenses(
  employeer_id: int,
  session: AsyncSession = Depends(get_db)
):
  employee_handler = EmployeeHandler(session)
  employeer = await employee_handler._get_employee_with_expenses(employeer_id)
  return employeer



@router.get(
  '/position_list/',
  status_code=status.HTTP_200_OK
)
async def get_employee_positions():
  positions =  positions_list()
  return positions