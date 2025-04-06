from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from apps.hotels_app.hotels.schemas import HotelWithRooms



from core.database import get_db
from .. import schemas
from ..handlers.program_handler import ProgramHandler
from apps.base.base_schemas import BaseMessageResponseModel
from apps.base.association_schemas import ProgramClientsPayments
from apps.staff.schemas import AppendExpensesToProgram



router = APIRouter(
  prefix='/programs',
  tags=['Programs']
)




@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ProgramBaseResponse
)
async def create_program(
  program_body: schemas.CreateProgramRequets,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  created_program = await program_handler._create_program(
    create_program_body=program_body
  )
  return created_program



@router.get(
  '/',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.ProgramBaseResponse]
)
async def get_all_programs(
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_list = await program_handler._get_programs_list()
  return program_list


@router.get(
  '/{program_slug}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ProgramBaseResponse
)
async def get_program_by_slug(
  program_slug: str,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program = await program_handler._get_program_by_slug(
    program_slug=program_slug
  )
  return program



@router.patch(
  '/{program_slug}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ProgramBaseResponse
)
async def update_program(
  program_slug: str,
  body: schemas.ProgramUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  updated_program = await program_handler._update_program(
    program_slug=program_slug,
    values=body
  )
  return updated_program



@router.get(
  '/clients/{program_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ProgramClientsResponse
)
async def get_program_clients(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_clients = await program_handler._get_program_clients(program_id)
  return program_clients




@router.post(
  '/append_client/',
  status_code=status.HTTP_201_CREATED,
  response_model=BaseMessageResponseModel
)
async def append_client_to_program(
  body: schemas.AppendClientToProgramRequest,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_client = await program_handler._append_client_to_program(body)
  return program_client



@router.post(
  '/delete_client',
  status_code=status.HTTP_200_OK
)
async def delete_client_from_program(
  body: schemas.DeleteClientFromProgramRequest,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  deleted_client = await program_handler._delete_client_from_program(body)
  return deleted_client



@router.get(
  '/program_clients_payments/{program_id}',
  status_code=status.HTTP_200_OK,
  response_model=List[ProgramClientsPayments]
)
async def get_program_clients_with_payments(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_clients = await program_handler._get_program_clients_with_payments(program_id)
  return program_clients



@router.get(
  '/program_hotels/{program_id}',
  status_code=status.HTTP_200_OK,
  response_model=List[HotelWithRooms]
)
async def get_program_hotels(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_hotels = await program_handler.get_program_hotels(program_id)
  return program_hotels



@router.post(
  '/program_expenses',
  status_code=status.HTTP_201_CREATED,
  responses={
    404: {'model': BaseMessageResponseModel}
  }
)
async def append_program_expenses(
  body: AppendExpensesToProgram,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_expenses = await program_handler._append_expensive_to_program(body)
  return program_expenses



@router.get(
  '/program_expenses/{program_id}',
  status_code=status.HTTP_200_OK,
  # response_model=schemas.ProgramExpensesResponse
)
async def get_program_expenses(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_expenses = await program_handler._get_program_expenses(program_id)
  return program_expenses



@router.delete(
  '/program_expenses',
  status_code=status.HTTP_200_OK
)
async def delete_program_expenses(
  body: AppendExpensesToProgram,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  deleted_program_expenses = await program_handler._delete_expensive_from_program(body)
  return deleted_program_expenses