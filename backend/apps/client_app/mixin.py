from sqlalchemy.ext.asyncio import AsyncSession

from .client.dals import ClientDAL


class ClientMixin:
  def __init__(self, session: AsyncSession):
    self.session = session
    self.client_dal = ClientDAL(self.session)
  
  
  async def get_client_data(self, client_id: int):
    client = await self.client_dal.get_client_by_id(client_id)
    return client
  
  
  async def check_client_slug(self, client_slug: str):
    client = await self.client_dal.get_client_by_slug(client_slug)
    return client