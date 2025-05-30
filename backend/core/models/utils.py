from enum import Enum


class ProgramStatus(str, Enum):
  AC = 'Active'
  CL = 'Closed'


class ClientProgramStatus(str, Enum):
  NC = 'Not Accepted'
  AC = 'Accepted'
  PF = 'Full Payed'



class ClientPorgramContractStatus(str, Enum):
  NS = 'Not Sended'
  SD = 'Sended'
  SG = 'Signed'
  


class ClientStatus(str, Enum):
  NW = 'New'
  RG = 'Regular'



class ClientDocumentType(str, Enum):
  PS = 'Passport'
  CT = 'Certificate'


class ClientFamilyRelation(str, Enum):
  HB = 'Husband'
  WF = 'Wife'
  CD = 'Child'
  FD = 'Friend'



class EmployeePosition(str, Enum):
  PM = 'Руководитель программы'
  AM = 'Астроном'
  AV = 'Астроном волонтер'
  LR = 'Лектор'
  PH = 'Фотограф'
  PV = 'Фотограф волонтер'
  CK = 'Повар'
  KV = 'Волонтер на кухню'


class ProgramPriceCategory(str, Enum):
  FT = 'Первый раз'
  WC = 'Были / пара'
  CM = 'Сообщество'
  ID = 'Индивидульная'


class PartnerCategory(str,  Enum):
  EX = 'Экскурсии'
  TF = 'Трансфер'
  OT = 'Остальное'



class StaticCategory(str, Enum):
  TRANSFER = 'transfer'
  FOOD = 'food'
  SALARY = 'salary'
  HABITATION = 'habitation'
  ORGANIZATION = 'organization'
  MARKETING = 'marketing'
  MARGIN = 'margin'
  MERCH = 'merch'



class ExpenseType(str, Enum):
  GR = 'group',
  CL = 'client'


class UserRole(str, Enum):
  AD = 'admin'
  MG = 'manager'
  SP = 'superuser'
  SZ = 'spritzer'