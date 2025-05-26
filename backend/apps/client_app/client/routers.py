from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from .handler import ClientHandler
from .. import schemas
from core.database import get_db
from apps.base.base_schemas import BaseMessageResponseModel


router = APIRouter(
  prefix='/base',
  tags=['Client Base']
)



@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.BaseShowClient
)
async def create_client(
  body: schemas.CreateClient,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  created_client = await client_handler._create_client(body)
  return created_client



@router.get(
  '/',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.BaseShowClient]
)
async def get_clients(
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  clients = await client_handler._get_clients_list()
  return clients


@router.get(
  '/{client_slug}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.BaseShowClient
)
async def get_client_by_slug(
  client_slug: str,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  client = await client_handler._get_client_by_slug(client_slug)
  return client



@router.patch(
  '/{client_id}',
  status_code=status.HTTP_200_OK
)
async def update_client_data(
  client_id: int,
  body: schemas.UpdateClientRequest,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  client = await client_handler._update_client(
    client_id=client_id,
    client_data=body
  )
  return client



@router.get(
  '/program/{client_slug}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ClientCurrentProgramBaseResponse,
  responses={
    404: {'model': BaseMessageResponseModel}
  }
)
async def get_client_current_program(
  client_slug: str,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  client_program = await client_handler._get_client_current_program(client_slug)
  return client_program


@router.get(
  '/program_profile_doc/{client_slug}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ClientCurrentProgramResponse
)
async def get_client_program_with_profile_and_doc(
  client_slug: str,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  client_program = await client_handler._get_client_current_program(
    client_slug=client_slug,
    flag=True
  )
  return client_program



@router.post(
  '/client_profile',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ClientProfileCreateResponse,
  responses={
    404: {'model': BaseMessageResponseModel},
    403: {'model': BaseMessageResponseModel}
  }
)
async def create_client_with_profile(
  body: schemas.CreateClientWithProfileRequest,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  client_with_profile = await client_handler._create_client_with_profile(
    client_data=body
  )
  return client_with_profile



@router.post(
  '/client_profile_doc',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ClientProfileDocCreateResponse,
  responses={
    404: {'model': BaseMessageResponseModel},
    403: {'model': BaseMessageResponseModel}
  }
)
async def create_client_with_profile_and_doc(
  body: schemas.CreateClientWithProfileAndDocRequest,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  client_profile_doc = await client_handler._create_client_profile_doc(
    client_data=body
  )
  return client_profile_doc



@router.get(
  '/client_profile_doc/{client_slug}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ShowClientProfileDocument
)
async def get_client_with_profile_and_doc(
  client_slug: str,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  client_data = await client_handler._get_client_with_profile_and_doc(
    client_slug=client_slug
  )
  return client_data


@router.post(
  '/append_client_to_prog_room/',
  status_code=status.HTTP_201_CREATED,
  response_model=BaseMessageResponseModel
)
async def append_client_to_program_room(
  body: schemas.AppendClientToProgramRoom,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  appended_client = await client_handler._append_client_to_program_room(body)
  return appended_client


@router.delete(
  '/delete_client_from_prog_room/',
  status_code=status.HTTP_200_OK,
  response_model=BaseMessageResponseModel
)
async def delete_client_from_program_room():...