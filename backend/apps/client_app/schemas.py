from typing import Optional, List, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.models.utils import ClientProgramStatus, ClientPorgramContractStatus

from datetime import date


from .client_profile.schemas import ProfileResponse, ProfileCreateRequestWithUser, ProfileResponse
from .client_doc.schemas import DocumentResponse, DocumentCreateRequestWithUser




class ClientProgramBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  id: int
  title: str
  start_date: date
  end_date: date
  place: str
  desc: str
  slug: str
  status: str




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
  profile: Optional[ProfileResponse] = None
  document: Optional[DocumentResponse] = None



class UpdateClientRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  last_name: Optional[str] = None
  name: Optional[str] = None
  second_name: Optional[str] = None
  phone: Optional[str] = None
  email: Optional[str] = None





class ClientCurrentProgramBaseResponse(BaseModel):
  id: int
  client_id: int
  status: ClientProgramStatus
  created_at: datetime
  price: Optional[int] = None
  contract_status: ClientPorgramContractStatus
  program: ClientProgramBase
  # client: BaseShowClient



class ClientCurrentProgramResponse(ShowClientProfileDocument):
  client_program_detail : Optional[List] = None

# class ClientCurrentProgramResponse(BaseModel):
#   id: int
#   client_id: int
#   status: ClientProgramStatus
#   created_at: datetime
#   price: int
#   contract_status: Optional[ClientPorgramContractStatus] = None
#   program: Optional[ClientProgramBase] = None
#   client: ShowClientProfileDocument


class CreateClientWithProfileRequest(CreateClient):
  profile: ProfileCreateRequestWithUser


class ClientProfileCreateResponse(BaseShowClient):
  profile: ProfileResponse


class CreateClientWithProfileAndDocRequest(CreateClientWithProfileRequest):
  doc: DocumentCreateRequestWithUser


class ClientProfileDocCreateResponse(ClientProfileCreateResponse):
  document: DocumentResponse


class AppendClientToProgramRoom(BaseModel):
  program_client_id: int
  program_room_id: int
  entry_date: date
  departue_date: date
  comment: Optional[str] = None
  no_sharing: Optional[bool] = False


class DeleteClientFromProgramRoom(BaseModel):
  program_client_id: int
  program_room_id: int
  model_config = ConfigDict(from_attributes=True)