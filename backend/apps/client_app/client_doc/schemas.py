from typing import Optional
from pydantic import BaseModel, ConfigDict
from core.models.utils import ClientDocumentType
from datetime import date


class DocumentBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  number: str
  series: str
  issued_by: str
  doc_type: ClientDocumentType
  date_of_issue: date
  client_id: int



class DocumnetResponse(DocumentBase):
  id: int


class CreateDocumentRequest(DocumentBase):
  pass


class UpdateDocumentRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  number: Optional[str] = None
  series: Optional[str] = None
  issued_by: Optional[str] = None
  doc_type: Optional[ClientDocumentType] = None
  date_of_issue: Optional[date] = None
  client_id: Optional[int] = None