from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from datetime import date

from apps.base.association_schemas import ProgramClientAssociationClientData



class ProgramBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  title: str
  start_date: date
  end_date: date
  place: str
  desc: str
  price: int



class CreateProgramRequets(ProgramBase):
  pass


class ProgramBaseResponse(ProgramBase):
  id: int
  slug: str
  status: str
  duration: Optional[int] = None
  
  class Config:
    from_attributes = True



class DeleteClientFromProgramRequest(BaseModel):
  client_id: int
  program_id: int



class AppendClientToProgramRequest(DeleteClientFromProgramRequest):
  price: Optional[int] = None



class ProgramResponseForAppendHotelAndRoom(BaseModel):
  id: int
  title: str
  place: str
  price: int





class ProgramClientsResponse(ProgramBaseResponse):
  program_clients_detail: Optional[List[ProgramClientAssociationClientData]] = []

