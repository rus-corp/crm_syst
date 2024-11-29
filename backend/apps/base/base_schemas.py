from pydantic import BaseModel



class BaseErrorResponseModel(BaseModel):
  message: str