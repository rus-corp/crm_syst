from apps.base.base_dal import BaseDAL
from datetime import date
from sqlalchemy import select, update

from core.models.client_models import ClientProfile
from core.models.utils import ClientStatus


class ClientProfileDAL(BaseDAL):
  model = ClientProfile
  
  async def create_profile(self, values):
    client_profile = await self.base_create_item(
      model=self.model,
      values=values
    )
    return client_profile
  
  
  async def get_client_profile(self, client_id: int):
    query = select(ClientProfile).where(ClientProfile.client_id == client_id)
    return await self.db_session.scalar(query)
  
  
  async def update_client_profile(self, client_id: int, values):
    query = update(ClientProfile).where(ClientProfile.client_id == client_id).values(**values).returning(ClientProfile)
    result = await self.db_session.scalar(query)
    return result
  
  