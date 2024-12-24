from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from .. import schemas
from ..handlers.employee_handler import EmployeeHandler


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