from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import date
from sqlalchemy import Enum as SQLEnum


from ..database import Base
from .utils import ProgramStatus, ProgramPriceCategory

if TYPE_CHECKING:
  from .client_models import Client
  from .hotels_models import Hotels, HotelRooms
  from .association_models import ProgramClients, ProgramRooms, ProgramClientRoom, ProgramPartners
  from .staff_models import Expenses




class Program(Base):
  __tablename__ = 'programs'
  
  title: Mapped[str] = mapped_column(index=True)
  start_date: Mapped[date]
  end_date: Mapped[date]
  place: Mapped[str]
  desc: Mapped[str]
  status: Mapped[ProgramStatus] = mapped_column(SQLEnum(ProgramStatus), default=ProgramStatus.AC)
  slug: Mapped[str] = mapped_column(unique=True)
  client_count: Mapped[int] = mapped_column(default=10)
  
  prices: Mapped['ProgramPrices'] = relationship(back_populates='program')
  program_clients_detail: Mapped[list['ProgramClients']] = relationship(back_populates='program')
  
  program_hotel_room: Mapped[list['ProgramRooms']] = relationship(back_populates='program')
  expenses: Mapped[List['Expenses']] = relationship(
    secondary='program_expenses',
    back_populates='programs'
  )
  program_partner: Mapped[list['ProgramPartners']] = relationship(back_populates='program')
  
  
  
  # program: Mapped[List['Hotels']] = relationship(secondary='program_rooms', back_populates='programs')
  # rooms: Mapped[List['HotelRooms']] = relationship(secondary='program_rooms', back_populates='programs')
  
  # clients_program_rooms: Mapped[List['Client']] = relationship(secondary='program_client_room', back_populates='program_clients_rooms')
  # room_program_client: Mapped[List['HotelRooms']] = relationship(secondary='program_client_room', back_populates='program_clients_rooms')
  
  # program_clients_rooms_assoc: Mapped[List['ProgramClientRoom']] = relationship(back_populates='program')
  
  def duration(self):
    return (self.end_date - self.start_date).days



class ProgramPrices(Base):
  __tablename__ = 'program_prices'
  
  # name: Mapped[ProgramPriceCategory] = mapped_column(SQLEnum(ProgramPriceCategory), default=ProgramPriceCategory.FT)
  # price: Mapped[int]
  base_price: Mapped[int]
  loayal_price: Mapped[int]
  comunity_price: Mapped[int]
  program_id: Mapped[int] = mapped_column(ForeignKey('programs.id'))
  
  program: Mapped['Program'] = relationship(back_populates='prices')