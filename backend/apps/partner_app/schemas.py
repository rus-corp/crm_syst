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
  partner_id: int


class BankAccountShowBase(BankAccountBase):
  id: int
  partner_id: int


class BankAccountShowUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  bank_name: Optional[str] = None
  bic: Optional[str] = None
  account_number: Optional[str] = None
  cor_account: Optional[str] = None


class PartnerServiceBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  service_name: str
  price: int


class PartnerServiceBaseResponse(PartnerServiceBase):
  id: int
  partner_id: int


class PartnerServiceCreateRequest(PartnerServiceBase):
  partner_id: int


class PartnerServiceUpdateRequest(PartnerServiceBase):
  service_name: Optional[str] = None
  price: Optional[int] = None



class CreatePartnerAndServiceRequest(PartnerBase):
  partner_services: List[PartnerServiceBase] = []


class CreatePartnerAndServiceResponse(PartnerBase):
  partner_services: List[PartnerServiceBaseResponse] = []


class PartnerBankServiceResponse(PartnerBaseShow):
  bank_account: Optional[BankAccountShowBase] = None
  service: Optional[List[PartnerServiceBaseResponse]] = []



# =========================== TypedDict ===================
class PartnerValues(TypedDict, total=False):
  id: int
  title: str
  law_title: str
  price: int
  contract_number: str
  bank_account_id: int