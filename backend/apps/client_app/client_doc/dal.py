from apps.base.base_dal import BaseDAL
from datetime import date
from sqlalchemy import select, update

from core.models.client_models import ClientDocument
from core.models.utils import ClientDocumentType



class ClientDocumentDAL(BaseDAL):

  async def create_client_document(
    self,
    series: str,
    number: str,
    date_of_issue: date,
    issued_by: str,
    client_id: int,
    doc_type: ClientDocumentType,
  ):
    client_document = ClientDocument(
      series=series,
      number=number,
      date_of_issue=date_of_issue,
      issued_by=issued_by,
      client_id=client_id,
      doc_type=doc_type
    )
    self.db_session.add(client_document)
    await self.db_session.commit()
    return client_document
  
  
  async def get_client_doc(self, client_id: int):
    query = select(ClientDocument).where(ClientDocument.client_id == client_id)
    return await self.db_session.scalar(query)
  
  
  async def update_client_doc(self, client_id: int):
    query = update(ClientDocument).where(ClientDocument.client_id == client_id).returning(ClientDocument)
    result = await self.db_session.scalar(query)
    return result