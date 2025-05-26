from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import AuthTokenResponse
from core.database import get_db
from .helpers import authenticate_user

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)

@router.post(
  '/login/',
  status_code=status.HTTP_201_CREATED,
  response_model=AuthTokenResponse
)
async def login(
  form_data: OAuth2PasswordRequestForm = Depends(), 
  session: AsyncSession = Depends(get_db),
):
  user_token = await authenticate_user(
    session=session,
    email=form_data.username,
    password=form_data.password
  )
  return AuthTokenResponse(**user_token)