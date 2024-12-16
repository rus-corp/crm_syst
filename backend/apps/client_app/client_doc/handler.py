from sqlalchemy.ext.asyncio import AsyncSession

from apps.base.base_handler import BaseHandler
from .dal import ClientDocumentDAL
from . import schemas
from ..mixin import ClientMixin
from apps.base.exceptions import AppBaseExceptions


class ClientDocumentHandler(ClientMixin, BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.doc_dal = ClientDocumentDAL(self.session)
  
  
  async def _create_client_doc(self, values: schemas.CreateDocumentRequest):
    async with self.session.begin():
      body_data = values.model_dump()
      has_client = await self.get_client_data(client_id=body_data['client_id'])
      if has_client is None:
        return AppBaseExceptions.item_not_found(item_data='Client')
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