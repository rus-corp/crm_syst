from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional, List

from apps.client_app.schemas import BaseShowClient
from apps.payments_app.schemas import ClientPaymentsResponse




class ProgramClientAssociationBase(BaseModel):
  id: int
  client_id: int
  program_id: int
  status: str
  created_at: date
  price: int
  contract_status: str



class ProgramClientAssociationClientData(ProgramClientAssociationBase):
  client: BaseShowClient


class ProgramClientsPayments(ProgramClientAssociationBase):
  client_program_payments: Optional[List[ClientPaymentsResponse]]



