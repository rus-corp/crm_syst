from typing import Optional, List, TypedDict
from pydantic import BaseModel, ConfigDict
from core.models.utils import PartnerCategory



class PartnerBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  title: str
  law_title: str
  price: int
  contract_number: Optional[str] = None
  service_name: str
  category: PartnerCategory



class PartnerBaseShow(PartnerBase):
  id: int


class CreatePartnerBaseRequest(PartnerBase):
  pass


class PartnerUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  title: Optional[str] = None
  law_title: Optional[str] = None
  price: Optional[int] = None
  contract_number: Optional[str] = None
  service_name: Optional[str] = None
  category: Optional[PartnerCategory] = None



class BankAccountBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  bank_name: str
  bic: str
  account_number: str
  cor_account: str

class BankAccountPartnerCreateRequest(BankAccountBase):
  pass


class BankAccountShowBase(BankAccountBase):
  id: int
  partner_id: int


class CreatePartnerAndBank(PartnerBase):
  bank_account: BankAccountPartnerCreateRequest


class PartnerBankCreateResponse(PartnerBaseShow):
  bank_account: BankAccountShowBase



# =========================== TypedDict ===================
class PartnerValues(TypedDict, total=False):
  id: int
  title: str
  law_title: str
  price: int
  contract_number: str
  bank_account_id: int