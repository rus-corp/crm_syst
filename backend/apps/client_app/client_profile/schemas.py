from typing import Optional
from pydantic import BaseModel, ConfigDict, model_validator
from core.models.utils import ClientStatus
from datetime import date







class ProfileBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  shirt_size: Optional[str] = None
  status: Optional[ClientStatus] = None
  city: Optional[str] = None
  client_id: int
  date_of_birth: Optional[date] = None
  


class ProfileResponse(ProfileBase):
  id: int
  community: bool
  nutrition_features: Optional[str] = None
  comment: Optional[str] = None



class ProfileCreateRequest(ProfileBase):
  community: Optional[bool] = None
  nutrition_features: Optional[str] = None
  comment: Optional[str] = None



class ProfileCreateRequestWithUser(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  shirt_size: str
  status: ClientStatus
  city: str
  date_of_birth: date
  community: Optional[bool] = None
  nutrition_features: Optional[str] = None
  comment: Optional[str] = None



class ProfileUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  shirt_size: Optional[str] = None
  status: Optional[ClientStatus] = None
  city: Optional[str] = None
  date_of_birth: Optional[date] = None
  nutrition_features: Optional[str] = None
  comment: Optional[str] = None
  community: Optional[bool] = None