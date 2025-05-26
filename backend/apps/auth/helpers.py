from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from datetime import datetime, timezone, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from .helpers import AuthJWT
from apps.users.dals import UserDAL

from .hasher import validate_password
from core.models.user_models import User
from core.database import get_db


auth_jwt = AuthJWT()


ACCESS_TOKEN_TYPE = 'access'
REFRESH_TOKEN_TYPE = 'refresh'


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')




def expire_func(token_type: str):
  if token_type == ACCESS_TOKEN_TYPE:
    return datetime.now(timezone.utc) + timedelta(minutes=30)
  if token_type == REFRESH_TOKEN_TYPE:
    return datetime.now(timezone.utc) + timedelta(days=30)





def encode_jwt(
  payload: dict,
  key: str = auth_jwt.private_key_path.read_text(),
  algorithm = auth_jwt.algorithm
):
  encoded = jwt.encode(
    payload,
    key,
    algorithm=algorithm,
  )
  return encoded



def decode_jwt(
  token: str | bytes,
  key: str = auth_jwt.public_key_path.read_text(),
  algorithm = auth_jwt.algorithm
):
  return jwt.decode(
    token,
    key,
    algorithms=[algorithm]
  )



async def get_user_from_token(
  token: str = Depends(oauth_scheme),
  session: AsyncSession = Depends(get_db)
):
  try:
    data = decode_jwt(token)
    user_id = data.get('sub')
    user_dal = UserDAL(session)
    user = await user_dal.get_user_by_id(user_id)
    if user is None:
      raise HTTPException(
          status_code=401,
          detail='Could not validate credentials'
        )
    return user
  except:
    raise HTTPException(
      status_code=401,
      detail='Could not validate credentials'
    )



def create_access_token(user: User):
  to_encode = {
    'sub': user.id.hex,
    'exp': expire_func(ACCESS_TOKEN_TYPE)
  }
  return encode_jwt(
    payload=to_encode,
  )


def create_refresh_token(user: User):
  to_encode = {
    'sub': user.id.hex,
    'exp': expire_func(REFRESH_TOKEN_TYPE)
  }
  return encode_jwt(
    payload=to_encode
  )




async def authenticate_user(
  session: AsyncSession,
  email: str,
  password: str
):
  user_dal = UserDAL(session)
  user: User = await user_dal.get_user_by_email(email)
  if user is None:
    raise HTTPException(
      status_code=404,
      detail='User not found'
    )
  if not validate_password(
    password=password,
    hashed_password=user.password.encode()
  ):
    raise HTTPException(
      status_code=401,
      detail='Incorrect password or email'
    )
  access_token = create_access_token(user)
  refresh_token = create_refresh_token(user)
  return {
    'access_token': access_token,
    'refresh_token': refresh_token
  }


async def get_current_user_refresh(
  token: str,
  session: AsyncSession
):
  try:
    data = decode_jwt(token)
    user_id = data.get('sub')
    user_dal = UserDAL(session)
    user_data = await user_dal.get_user_by_id(user_id)
    return user_data
  except:
    raise HTTPException(
      status_code=401,
      detail='Could not validate credentials'
    )