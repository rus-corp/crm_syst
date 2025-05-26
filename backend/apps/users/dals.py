from ..base.base_dal import BaseDAL
from core.models.user_models import User
from sqlalchemy import select

class UserDAL(BaseDAL):
  model = User
  
  async def create_user(
    self,
    email: str,
    first_name: str,
    last_name: str,
    password: str,
    role: str
  ):
    new_user = self.model(
      email=email,
      first_name=first_name,
      last_name=last_name,
      password=password,
      role=role
    )
    self.db_session.add(new_user)
    await self.db_session.commit()
    return new_user
  
  
  async def get_user_by_id(self, user_id: int):
    return await self.base_get_one_item(
      model=self.model,
      item_id=user_id
    )
  
  
  async def get_user_by_email(self, email: str):
    query = select(self.model).where(self.model.email == email)
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_all_users(self):
    return await self.base_get_all_items(self.model)
  
  
  async def update_user_by_id(self, user_id: int, values):
    return await self.base_update_item(
      model=self.model,
      item_id=user_id,
      values=values
    )
  
  
  async def delete_user_by_id(self, user_id: int):
    return await self.base_delete_item(
      model=self.model,
      item_id=user_id
    )