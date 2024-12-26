from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from datetime import date

from apps.base.association_schemas import ProgramClientAssociationClientData
from apps.staff.schemas import ExpenseFullResponse



class ProgramBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  title: str
  start_date: date
  end_date: date
  place: str
  desc: str



class CreateProgramRequets(ProgramBase):
  pass


class ProgramUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  title: Optional[str] = None
  start_date: Optional[date] = None
  end_date: Optional[date] = None
  place: Optional[str] = None
  desc: Optional[str] = None
  price: Optional[int] = None



class ProgramBaseResponse(ProgramBase):
  id: int
  slug: str
  status: str
  duration: Optional[int] = None


class ProgramBaseWithoutDurationResponse(ProgramBase):
  id: int
  slug: str
  status: str


class DeleteClientFromProgramRequest(BaseModel):
  client_id: int
  program_id: int



class AppendClientToProgramRequest(DeleteClientFromProgramRequest):
  price: Optional[int] = None



class ProgramResponseForAppendHotelAndRoom(BaseModel):
  id: int
  title: str
  place: str


class ProgramClientsResponse(ProgramBaseResponse):
  program_clients_detail: Optional[List[ProgramClientAssociationClientData]] = []



class ProgramExpensesResponse(ProgramBaseWithoutDurationResponse):
  expenses: Optional[List[ExpenseFullResponse]] = []