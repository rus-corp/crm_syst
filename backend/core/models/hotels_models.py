from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload, Session
from sqlalchemy import ForeignKey, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import Base

if TYPE_CHECKING:
  from .program_models import Program
  from .client_models import Client
  from .association_models import ProgramClientRoom, ProgramRooms






class Hotels(Base):
  __tablename__ = 'hotel'
  title: Mapped[str] = mapped_column(index=True)
  address: Mapped[str]
  contacts: Mapped[str]
  desc: Mapped[str] = mapped_column(nullable=True)
  city: Mapped[str]
  email: Mapped[str] = mapped_column(unique=True, index=True)
  
  rooms: Mapped[List['HotelRooms']] = relationship(back_populates='hotel')
  program_hotel_room: Mapped[list['ProgramRooms']] = relationship(back_populates='hotel')
  
  # programs: Mapped[List['Program']] = relationship(secondary='program_rooms', back_populates='hotels')
  
  async def get_room_volumes(self, session: AsyncSession):
    res = await session.execute(
      select(HotelRooms.room_volume).where(HotelRooms.hotel_id == self.id)
    )
    room_vol = sum(row[0] for row in res.all())
    return room_vol





class HotelRooms(Base):
  __tablename__ = 'hotel_rooms'
  room_type: Mapped[str]
  room_price: Mapped[int]
  room_volume: Mapped[int]
  hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
  
  hotel: Mapped[Hotels] = relationship(back_populates='rooms')
  program_hotel_room: Mapped[list['ProgramRooms']] = relationship(back_populates='room')
  # programs: Mapped[List['Program']] = relationship(secondary='program_rooms', back_populates='rooms')
  
  # program_clients_rooms: Mapped[List['Program']] = relationship(secondary='program_client_room', back_populates='room_program_client')
  # room_clients: Mapped[List['Client']] = relationship(secondary='program_client_room', back_populates='client_rooms')
  
  # program_client_rooms_assoc: Mapped[List['ProgramClientRoom']] = relationship(back_populates='room')



