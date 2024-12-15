from sqlalchemy.ext.asyncio import AsyncSession

from apps.base.base_handler import BaseHandler
from .dal import ClientDocumentDAL
from . import schemas


class ClientDocumentHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.doc_dal = ClientDocumentDAL(self.session)
  
  
  async def _create_client_doc(self, values: schemas.CreateDocumentRequest):
    async with self.session.begin():
      body_data = values.model_dump()
      client_doc = await self.doc_dal.create_client_document(body_data)
      return client_doc
  
  
  async def _get_client_doc(self, client_id: int):
    client_doc = await self.doc_dal.get_client_doc(client_id)
    return client_doc
  
  
  async def _update_client_doc(self, client_id: int, values: schemas.UpdateDocumentRequest):
    async with self.session.begin():
      body_data = values.model_dump(exclude_none=True)
      client_doc = await self.doc_dal.update_client_doc(
        client_id=client_id,
        values=body_data
      )
      return client_doc