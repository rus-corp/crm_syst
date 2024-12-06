from pydantic import BaseModel, ConfigDict
from datetime import date



class CreateClientPaymentBody(BaseModel):
  client_id: int
  program_id: int
  amount: int


class ClientPaymentsResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  client_program_id: int
  amount: int
  payment_date: date