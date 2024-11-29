from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func, UniqueConstraint
from sqlalchemy import Enum as SQLEnum
from datetime import datetime, date



from ..database import Base
from .utils import ClientProgramStatus


from .hotels_models import Hotels, HotelRooms
from .payment_models import ClientProgramPayment

if TYPE_CHECKING:
  from .client_models import Client
  from .program_models import Program





class ProgramClients(Base):
  __tablename__ = 'program_clients'
  __table_args__ = (UniqueConstraint('program_id', 'client_id'),)
  
  client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
  program_id: Mapped[int] = mapped_column(ForeignKey('program.id'))
  price: Mapped[int] = mapped_column(nullable=True)
  status: Mapped[ClientProgramStatus] = mapped_column(SQLEnum(ClientProgramStatus), default=ClientProgramStatus.NOT_ACCEPTED)
  created_at: Mapped[datetime] = mapped_column(server_default=func.now())
  
  program: Mapped["Program"] = relationship(back_populates='program_clients_detail')
  client: Mapped["Client"] = relationship(back_populates='client_program_detail')
  
  client_program_payments: Mapped[list[ClientProgramPayment]] = relationship(back_populates='client_program')







class ProgramRooms(Base):
  __tablename__ = 'program_rooms'
  __table_args__ = (UniqueConstraint('program_id', 'hotel_id', 'room_id'),)
  
  program_id: Mapped[int] = mapped_column(ForeignKey('program.id'))
  hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
  room_id: Mapped[int] = mapped_column(ForeignKey('hotel_rooms.id'))
  
  program: Mapped['Program'] = relationship(back_populates='program_hotel_room')
  hotel: Mapped[Hotels] = relationship(back_populates='program_hotel_room')
  room: Mapped[HotelRooms] = relationship(back_populates='program_hotel_room')
  



# class ProgramClientRoom(Base):
#   __tablename__ = 'program_client_room'
#   __table_args__ = (UniqueConstraint('client_id', 'program_id', 'room_id'),)
#   client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
#   program_id: Mapped[int] = mapped_column(ForeignKey('program.id'))
#   room_id: Mapped[int] = mapped_column(ForeignKey('hotel_rooms.id'))
  
#   enty_date:Mapped[date]
#   departue_date: Mapped[date]
  
#   program: Mapped[Program] = relationship(back_populates='program_clients_rooms_assoc')
#   client: Mapped[Client] = relationship(back_populates='program_client_rooms_assoc')
#   room: Mapped[HotelRooms] = relationship(back_populates='program_client_rooms_assoc')