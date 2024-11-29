from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, ForeignKey
from datetime import datetime, date
from sqlalchemy import Enum as SQLEnum

from ..database import Base

if TYPE_CHECKING:
  from .association_models import ProgramClients



class ClientProgramPayment(Base):
  __tablename__ = 'client_Program_payment'
  
  client_program_id: Mapped[int] = mapped_column(ForeignKey('program_clients.id'))
  amount: Mapped[int]
  payment_date: Mapped[date] = mapped_column(server_default=func.now())
  
  client_program: Mapped['ProgramClients'] = relationship(back_populates='client_program_payments')