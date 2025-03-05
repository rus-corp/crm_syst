from pydantic import BaseModel



class BaseMessageResponseModel(BaseModel):
  message: str