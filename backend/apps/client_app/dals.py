from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy import select, update, delete


from ..base.base_dal import BaseDAL


from core.models.client_models import Client



class ClientDAL(BaseDAL):
  async def create_client(
    self,
    name:(str),
    last_name:(str),
    second_name:(str),
    phone:(str),
    email:(str),
    slug:(str)
  ):
    new_client = Client(
      name=name,
      last_name=last_name,
      second_name=second_name,
      phone=phone,
      email=email,
      slug=slug,
    )
    self.db_session.add(new_client)
    await self.db_session.commit()
    return new_client
  
  
  async def get_clients(self):
    return await self.base_get_all_items(Client)
  
  
  async def get_client_by_id(self, client_id):
    query = select(Client).where(Client.id == client_id)
    result = await self.db_session.scalar(query)
    return result