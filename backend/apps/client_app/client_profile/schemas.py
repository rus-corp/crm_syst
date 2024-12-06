from typing import Optional
from pydantic import BaseModel, ConfigDict
from core.models.utils import ClientStatus
from datetime import date







class ProfileBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  shirt_size: str
  status: ClientStatus
  city: str
  client_id: int
  date_of_birth: date


class ProfileResponse(ProfileBase):
  id: int
  nutrition_features: Optional[str] = None
  comment: Optional[str] = None


class ProfileCreateRequest(ProfileBase):
  nutrition_features: Optional[str] = None
  comment: Optional[str] = None


class ProfilUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  shirt_size: Optional[str] = None
  status: Optional[ClientStatus] = None
  city: Optional[str] = None
  client_id: Optional[int] = None
  date_of_birth: Optional[date] = None
  nutrition_features: Optional[str] = None
  comment: Optional[str] = None