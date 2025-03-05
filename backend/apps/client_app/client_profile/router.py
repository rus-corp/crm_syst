from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from . import schemas
from .handler import ClientProfileHandler
from apps.base.base_schemas import BaseMessageResponseModel



router = APIRouter(
  prefix='/profile',
  tags=['Client Profile']
)



@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ProfileResponse,
  responses={
    404: {'model': BaseMessageResponseModel}
  }
)
async def create_client_profile(
  body: schemas.ProfileCreateRequest,
  session: AsyncSession = Depends(get_db)
):
  profile_handler  = ClientProfileHandler(session)
  client_profile = await profile_handler._create_client_profile(body)
  return client_profile



@router.get(
  '/{client_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ProfileResponse
)
async def get_client_profile(
  client_id: int,
  session: AsyncSession = Depends(get_db)
):
  profile_handler  = ClientProfileHandler(session)
  client_profile = await profile_handler._get_client_profile(client_id)
  return client_profile



@router.patch(
  '/{client_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ProfileResponse
)
async def update_client_profile(
  client_id: int,
  body: schemas.ProfileUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  profile_handler  = ClientProfileHandler(session)
  client_profile = await profile_handler._update_client_profile(
    client_id=client_id,
    values=body
  )
  return client_profile