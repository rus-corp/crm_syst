from pydantic import BaseModel, ConfigDict, EmailStr



class UserAuthSchema(BaseModel):
  email: EmailStr
  password: bytes


class AuthTokenResponse(BaseModel):
  access_token: str
  refresh_token: str
  token_type: str = 'bearer'