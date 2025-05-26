from typing import Optional
from pydantic import BaseModel, ConfigDict

from core.models.utils import UserRole


class UserBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  email: str
  first_name: str
  last_name: str
  password: str
  role: UserRole = UserRole.MG


class UserAdminCreateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  email: str
  first_name: str
  last_name: str
  password: str

class UserBaseResponse(UserBase):
  id : int


class CreateUserResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  email: str
  first_name: str
  last_name: str
  role: UserRole


class UpdateUserRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  email: Optional[str] = None
  first_name: Optional[str] = None
  last_name: Optional[str] = None
  password: Optional[str] = None
  role: Optional[str] = None