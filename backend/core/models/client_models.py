from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String, ForeignKey, UniqueConstraint, Index
from datetime import datetime, date
from sqlalchemy import Enum as SQLEnum

from ..database import Base
from .utils import ClientStatus, ClientDocumentType, ClientFamilyRelation






if TYPE_CHECKING:
  from .program_models import Program
  from .association_models import ProgramClients, ProgramClientRoom
  from .hotels_models import HotelRooms








class BaseClient(Base):
  __abstract__ = True
  
  name: Mapped[str]
  last_name: Mapped[str]
  second_name: Mapped[str] = mapped_column(nullable=True)





class Client(BaseClient):
  __tablename__ = 'client'
  __table_args__ = (Index('client_indx', 'last_name', 'name'),)
  
  phone: Mapped[str]
  email: Mapped[str]
  slug: Mapped[str] = mapped_column(unique=True)
  updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=func.now(), server_onupdate=func.now())
  created_at: Mapped[datetime] = mapped_column(server_default=func.now())
  
  document: Mapped['ClientDocument'] = relationship(back_populates='client')
  profile: Mapped['ClientProfile'] = relationship(back_populates='client')
  client_family: Mapped[list['ClientFamily']] = relationship(back_populates='client')
  
  client_program_detail: Mapped[list['ProgramClients']] = relationship(back_populates='client')
  
  # program_clients_rooms: Mapped[List['Program']] = relationship(secondary='program_client_room', back_populates='clients_program_rooms')
  # client_rooms: Mapped[List['HotelRooms']] = relationship(secondary='program_client_room', back_populates='room_clients')
  # program_client_rooms_assoc: Mapped[List['ProgramClientRoom']] = relationship(back_populates='client')




class ClientProfile(Base):
  __tablename__ = 'client_profile'
  __table_args__ = (UniqueConstraint('client_id'),)
  
  shirt_size: Mapped[str]
  status: Mapped[ClientStatus] = mapped_column(SQLEnum(ClientStatus), default=ClientStatus.NEW)
  nutrition_features: Mapped[str]
  comment: Mapped[str] = mapped_column(nullable=True)
  city: Mapped[str]
  date_of_birth: Mapped[date]
  
  client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
  client: Mapped[Client] = relationship(back_populates='profile')
  client_family: Mapped['ClientFamily'] = relationship(back_populates='profile')




class ClientDocument(Base):
  __tablename__ = 'client_document'
  __table_args__ = (UniqueConstraint('client_id'),)
  
  doc_type: Mapped[ClientDocumentType] = mapped_column(SQLEnum(ClientDocumentType))
  series: Mapped[str] = mapped_column(String(10))
  number: Mapped[str] = mapped_column(String(30))
  date_of_issue: Mapped[date]
  issued_by: Mapped[str] = mapped_column(String(255))
  
  client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
  client: Mapped[Client] = relationship(back_populates='document')
  client_family: Mapped['ClientFamily'] = relationship(back_populates='document')




class ClientFamily(BaseClient):
  __tablename__ = 'client_family'
  __table_args__ = (UniqueConstraint('profile_id', 'document_id'),)
  
  FAMILY_RELATION_CHOICES = (
    ('HB', 'Муж'),
    ('WF', 'Жена'),
    ('CH', 'Ребенок'),
    ('FR', 'Друг'),
  )
  client_relation:Mapped[ClientFamilyRelation] = mapped_column(SQLEnum(ClientFamilyRelation), nullable=True)
  client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
  profile_id: Mapped[int] = mapped_column(ForeignKey('client_profile.id'))
  document_id: Mapped[int] = mapped_column(ForeignKey('client_document.id'))
  
  profile: Mapped[ClientProfile] = relationship(back_populates='client_family')
  document: Mapped[ClientDocument] = relationship(back_populates='client_family')
  client: Mapped[Client] = relationship(back_populates='client_family')