from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.database import get_db
from core.models.user_models import User
from .handler import UserHandler
from . import schemas
from apps.auth.helpers import get_user_from_token



router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.UserBaseResponse
)
async def create_user(
  user: schemas.UserBase,
  session: AsyncSession = Depends(get_db),
  current_user: User = Depends(get_user_from_token)
):
  user_handler = UserHandler(session)
  return await user_handler._create_user(user)




@router.get(
  '/', status_code=status.HTTP_200_OK,
  response_model=list[schemas.UserBaseResponse]
)
async def get_all_users(
  session: AsyncSession = Depends(get_db),
  current_user: User = Depends(get_user_from_token)
):
  user_handler = UserHandler(session, current_user)
  return await user_handler._get_all_users()



@router.get(
  '/{user_id}',
  status_code=status.HTTP_200_OK
)
async def get_user_by_id(
  user_id: int,
  session: AsyncSession = Depends(get_db),
  current_user: User = Depends(get_user_from_token)
):
  user_handler = UserHandler(session, current_user)
  return await user_handler._get_user_by_id(user_id)



@router.patch(
  '/{user_id}',
  status_code=status.HTTP_200_OK
)
async def update_user(
  user_id: int,
  body: schemas.UpdateUserRequest,
  session: AsyncSession = Depends(get_db),
  current_user: User = Depends(get_user_from_token)
):
  user_handler = UserHandler(session, current_user)
  return await user_handler._update_user(user_id, body)



@router.delete(
  '/{user_id}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
  user_id: int,
  session: AsyncSession = Depends(get_db),
  current_user: User = Depends(get_user_from_token)
):
  user_handler = UserHandler(session, current_user)
  return await user_handler._delete_user(user_id)


@router.post(
  '/super_user/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.UserBaseResponse
)
async def create_super_user(
  body: schemas.UserAdminCreateRequest,
  session: AsyncSession = Depends(get_db),
):
  user_handler = UserHandler(session)
  return await user_handler._create_super_user(body)