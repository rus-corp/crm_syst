from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status


from core.database import get_db
from . import schemas
from .handlers import ProgramHandler




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
  '/clients/{program_id}',
  status_code=status.HTTP_200_OK
)
async def get_program_clients(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_clients = await program_handler._get_program_clients(program_id)
  return program_clients




@router.post(
  '/append',
  status_code=status.HTTP_201_CREATED
)
async def appen_client_to_program(
  body: schemas.AppendClientToProgramRequest,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_client = await program_handler._append_client_to_program(body)
  return program_client



@router.post(
  '/delete',
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
  status_code=status.HTTP_200_OK
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
  status_code=status.HTTP_200_OK
)
async def get_program_hotels(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_hotels = await program_handler.get_program_hotels(program_id)
  return program_hotels