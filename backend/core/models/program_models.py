from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import Enum as SQLEnum


from ..database import Base
from .utils import ProgramStatus

if TYPE_CHECKING:
  from .client_models import Client
  from .hotels_models import Hotels, HotelRooms
  from .association_models import ProgramClients, ProgramRooms




class Program(Base):
  __tablename__ = 'program'
  
  title: Mapped[str]
  start_date: Mapped[date]
  end_date: Mapped[date]
  place: Mapped[str]
  desc: Mapped[str]
  price: Mapped[int]
  status: Mapped[ProgramStatus] = mapped_column(SQLEnum(ProgramStatus), default=ProgramStatus.ACTIVE)
  slug: Mapped[str] = mapped_column(unique=True)
  
  program_clients_detail: Mapped[list['ProgramClients']] = relationship(back_populates='program')
  
  program_hotel_room: Mapped[list['ProgramRooms']] = relationship(back_populates='program')
  # program: Mapped[List['Hotels']] = relationship(secondary='program_rooms', back_populates='programs')
  # rooms: Mapped[List['HotelRooms']] = relationship(secondary='program_rooms', back_populates='programs')
  
  # clients_program_rooms: Mapped[List['Client']] = relationship(secondary='program_client_room', back_populates='program_clients_rooms')
  # room_program_client: Mapped[List['HotelRooms']] = relationship(secondary='program_client_room', back_populates='program_clients_rooms')
  
  # program_clients_rooms_assoc: Mapped[List['ProgramClientRoom']] = relationship(back_populates='program')
  
  def duration(self):
    return (self.end_date - self.start_date).days


