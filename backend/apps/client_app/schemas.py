from typing import Optional, List
from pydantic import BaseModel, ConfigDict



class ClientBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  name: str
  last_name: str
  second_name: Optional[str] = None
  phone: str
  email: str


class CreateClient(ClientBase):
  pass