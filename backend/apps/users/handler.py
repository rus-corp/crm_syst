from ..base.base_handler import BaseHandler
from .dals import UserDAL

from config import settings

from .schemas import UserBase, UpdateUserRequest
from core.models.user_models import User
from config import super_user_email
from apps.auth.hasher import hash_password
from apps.base.exceptions import AppBaseExceptions

class UserHandler(BaseHandler):
  def __init__(self, session, current_user: User=None):
    super().__init__(session, current_user)
    self.user_dal = UserDAL(self.session)
  
  
  async def _create_super_user(self, body: UserBase):
    async with self.session.begin():
      if body.email == settings.super_user_email:
        body_data = body.model_dump()
        body_data['password'] = hash_password(body_data['password']).decode()
        try:
          user = await self.user_dal.create_user(**body_data)
          return user
        except Exception as e:
          raise Exception(f"Error creating superuser: {e}")
      else:
        raise AppBaseExceptions.access_denied()
  
  
  async def _create_user(self, body: UserBase):
      if self.permissions.superuser_permission():
        async with self.session.begin():
          body_data = body.model_dump()
          body_data['password'] = hash_password(body_data['password']).decode()
          try:
            user = await self.user_dal.create_user(**body_data)
            return user
          except Exception as e:
            raise Exception(f"Error creating user: {e}")
      else:
        raise AppBaseExceptions.access_denied()
  
  
  async def _get_all_users(self):
    if self.permissions.superuser_permission():
      user_list = await self.user_dal.get_all_users()
      return list(user_list)
    else:
      raise AppBaseExceptions.access_denied()
  
  
  async def _get_user_by_id(self, user_id: int):
    if self.permissions.superuser_permission():
      user = await self.user_dal.get_user_by_id(user_id)
      return user
    else:
      raise AppBaseExceptions.access_denied()
  
  
  async def _update_user(self, user_id: int, body: UpdateUserRequest):
      if self.permissions.superuser_permission():
        async with self.session.begin():
          body_data = body.model_dump(exclude_none=True)
          updated_user = await self.user_dal.update_user_by_id(
            user_id=user_id,
            values=body_data
          )
          return updated_user
      else:
        raise AppBaseExceptions.access_denied()
  
  
  async def _delete_user(self, user_id: int):
    if self.permissions.superuser_permission():
      async with self.session.begin():
        deleted_user = await self.user_dal.delete_user_by_id(user_id)
        return deleted_user
    else:
      raise AppBaseExceptions.access_denied()