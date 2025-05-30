from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func, UniqueConstraint
from sqlalchemy import Enum as SQLEnum
from datetime import datetime, date



from ..database import Base
from .utils import ClientProgramStatus, ClientPorgramContractStatus


from .hotels_models import Hotels, HotelRooms
from .payment_models import ClientProgramPayment
from .staff_models import Expenses

if TYPE_CHECKING:
  from .client_models import Client
  from .program_models import Program
  from .partners_models import Partner, PartnerService





class ProgramClients(Base):
  __tablename__ = 'program_clients'
  __table_args__ = (UniqueConstraint('program_id', 'client_id'),)
  
  client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
  program_id: Mapped[int] = mapped_column(ForeignKey('programs.id'))
  price: Mapped[int] = mapped_column(nullable=True)
  status: Mapped[ClientProgramStatus] = mapped_column(SQLEnum(ClientProgramStatus), default=ClientProgramStatus.NC)
  contract_status: Mapped[ClientPorgramContractStatus] = mapped_column(SQLEnum(ClientPorgramContractStatus), default=ClientPorgramContractStatus.NS)
  created_at: Mapped[datetime] = mapped_column(server_default=func.now())
  
  program: Mapped["Program"] = relationship(back_populates='program_clients_detail')
  client: Mapped["Client"] = relationship(back_populates='client_program_detail')
  
  program_client_room: Mapped['ProgramClientRoom'] = relationship(back_populates='program_clients')
  
  client_program_payments: Mapped[list[ClientProgramPayment]] = relationship(back_populates='client_program')




class ProgramRooms(Base):
  __tablename__ = 'program_rooms'
  __table_args__ = (UniqueConstraint('program_id', 'hotel_id', 'room_id'),)
  
  program_id: Mapped[int] = mapped_column(ForeignKey('programs.id'))
  hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
  room_id: Mapped[int] = mapped_column(ForeignKey('hotel_rooms.id'))
  
  program: Mapped['Program'] = relationship(back_populates='program_hotel_room')
  hotel: Mapped[Hotels] = relationship(back_populates='program_hotel_room')
  room: Mapped[HotelRooms] = relationship(back_populates='program_hotel_room')
  
  program_client_room: Mapped['ProgramClientRoom'] = relationship(back_populates='program_room')




class ProgramClientRoom(Base):
  __tablename__ = 'program_client_room'
  __table_args__ = (UniqueConstraint('program_client_id', 'program_room_id'),)
  
  program_client_id: Mapped[int] = mapped_column(ForeignKey('program_clients.id'))
  program_room_id: Mapped[int] = mapped_column(ForeignKey('program_rooms.id'))
  entry_date:Mapped[date]
  departue_date: Mapped[date]
  comment: Mapped[str] = mapped_column(nullable=True)
  no_sharing: Mapped[bool] = mapped_column(default=False)
  
  program_clients: Mapped[ProgramClients] = relationship(back_populates='program_client_room')
  program_room: Mapped[ProgramRooms] = relationship(back_populates='program_client_room')



class ProgramExpenses(Base):
  __tablename__ = 'program_expenses'
  program_id: Mapped[int] = mapped_column(ForeignKey('programs.id'))
  expenses_id: Mapped[int] = mapped_column(ForeignKey('expenses.id'))


class ProgramPartners(Base):
  __tablename__ = 'program_partners'
  program_id: Mapped[int] = mapped_column(ForeignKey('programs.id'))
  partner_id: Mapped[int] = mapped_column(ForeignKey('partners.id'))
  service_id: Mapped[int] = mapped_column(ForeignKey('partner_services.id'))
  
  partner: Mapped['Partner'] = relationship(back_populates='program_partner')
  service: Mapped['PartnerService'] = relationship(back_populates='program_partner')
  program: Mapped['Program'] = relationship(back_populates='program_partner')