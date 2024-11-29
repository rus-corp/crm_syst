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