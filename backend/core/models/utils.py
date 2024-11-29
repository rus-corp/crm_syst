from enum import Enum


class ProgramStatus(str, Enum):
  ACTIVE = 'Active'
  CLOSED = 'Closed'


class ClientProgramStatus(str, Enum):
  NOT_ACCEPTED = 'Not Accepted'
  ACCEPTED = 'Accepted'
  PAID_FULL = 'Full Payed'


class ClientStatus(str, Enum):
  NEW = 'New'
  REGULAR = 'Regular'



class ClientDocumentType(str, Enum):
  PASSPORT = 'Passport'
  CERTIFICATE = 'Certificate'


class ClientFamilyRelation(str, Enum):
  HUSBAND = 'Husband'
  WIFE = 'Wife'
  CHILD = 'Child'
  FRIEND = 'Friend'