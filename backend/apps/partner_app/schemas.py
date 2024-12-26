from typing import Optional, List, TypedDict
from pydantic import BaseModel, ConfigDict



class PartnerBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  title: str
  law_title: str
  price: int
  contract_number: Optional[str] = None



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



class BankAccountBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  bank_name: str
  bic: str
  account_number: str
  cor_account: str


class BankAccountShowBase(BankAccountBase):
  id: int


class CreatePartnerAndBank(PartnerBase):
  bank_account: BankAccountBase


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