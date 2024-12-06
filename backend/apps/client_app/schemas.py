from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.models.utils import ClientProgramStatus, ClientPorgramContractStatus
from apps.program_app.schemas import ClientProgramResponse
from datetime import date


from .client_profile.schemas import ProfileResponse
from .client_doc.schemas import DocumnetResponse




class ClientBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  name: str
  last_name: str
  second_name: Optional[str] = None
  phone: str
  email: str


class CreateClient(ClientBase):
  pass


class BaseShowClient(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  id: int
  last_name: str
  name: str
  second_name: Optional[str]
  phone: str
  email: str
  created_at: datetime
  updated_at: datetime
  slug: str


class ShowClientProfileDocument(BaseShowClient):
  profile: ProfileResponse
  document: DocumnetResponse



class ClientCurrentProgramBaseResponse(BaseModel):
  client_id: int
  status: ClientProgramStatus
  created_at: datetime
  price: int
  contract_status: ClientPorgramContractStatus
  program: ClientProgramResponse
  client: BaseShowClient


class ClientCurrentProgramResponse(BaseModel):
  id: int
  client_id: int
  status: ClientProgramStatus
  created_at: datetime
  price: int
  contract_status: ClientPorgramContractStatus
  program: ClientProgramResponse
  client: ShowClientProfileDocument
