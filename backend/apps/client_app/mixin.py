from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from .client.dals import ClientDAL
from ..utils.slug import create_slug


class ClientMixin:
  def __init__(self, session: AsyncSession):
    self.session = session
    self.client_dal = ClientDAL(self.session)
  
  
  async def get_client_data(self, client_id: int):
    client = await self.client_dal.get_client_by_id(client_id)
    return client
  
  
  async def check_and_create_client_slug(self, client_data: dict):
    unique_slug = create_slug(client_data['name'] + client_data['last_name'])
    client = await self.client_dal.get_client_by_slug(unique_slug)
    if client:
      unique_slug = create_slug(
        client_data['name'] 
        + client_data['last_name'] 
        + client_data['second_name'] 
        + (datetime.now()).strftime('%Y-%m-%d').split(' ')[0]
      )
    return unique_slug