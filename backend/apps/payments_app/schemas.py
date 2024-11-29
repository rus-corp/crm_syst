from pydantic import BaseModel, ConfigDict




class CreateClientPaymentBody(BaseModel):
  client_id: int
  program_id: int
  amount: int