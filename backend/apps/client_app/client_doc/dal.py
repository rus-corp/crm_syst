from apps.base.base_dal import BaseDAL
from datetime import date
from sqlalchemy import select, update

from core.models.client_models import ClientDocument
from core.models.utils import ClientDocumentType



class ClientDocumentDAL(BaseDAL):
  model = ClientDocument

  async def create_client_document(self, values):
    client_document = await self.base_create_item(
      model=self.model,
      values=values
    )
    return client_document
  
  
  async def get_client_doc(self, client_id: int):
    query = select(ClientDocument).where(ClientDocument.client_id == client_id)
    return await self.db_session.scalar(query)
  
  
  async def update_client_doc(self, client_id: int, values):
    query = update(ClientDocument).where(ClientDocument.client_id == client_id).values(**values).returning(ClientDocument)
    result = await self.db_session.scalar(query)
    return result