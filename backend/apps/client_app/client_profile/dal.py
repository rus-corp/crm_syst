from apps.base.base_dal import BaseDAL
from datetime import date
from sqlalchemy import select, update

from core.models.client_models import ClientProfile
from core.models.utils import ClientStatus


class ClientProfileDAL(BaseDAL):
  
  async def create_profile(
    self,
    shirt_size: str,
    city: str,
    date_of_birth: date,
    client_id: int,
    status: str = ClientStatus.NW,
    comment: str = None,
    nutrition_features: str = None,
  ):
    client_profile = ClientProfile(
      shirt_size=shirt_size,
      city=city,
      date_of_birth=date_of_birth,
      client_id=client_id,
      status=status,
      comment=comment,
      nutrition_features=nutrition_features
    )
    self.db_session.add(client_profile)
    await self.db_session.commit()
    return client_profile
  
  
  async def get_client_profile(self, client_id: int):
    query = select(ClientProfile).where(ClientProfile.client_id == client_id)
    return await self.db_session.scalar(query)
  
  async def update_client_profile(self, client_id: int, **values):
    query = update(ClientProfile).where(ClientProfile.client_id == client_id).values(values).returning(ClientProfile)
    result = await self.db_session.scalar(query)
    return result
  
  