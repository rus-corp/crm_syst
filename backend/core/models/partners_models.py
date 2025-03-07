from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey


from ..database import Base

from .utils import PartnerCategory



class BankAccount(Base):
  __tablename__ = 'bank_accounts'
  bank_name: Mapped[str]
  bic: Mapped[str]
  account_number: Mapped[str]
  cor_account: Mapped[str]
  
  partner_id: Mapped[int] = mapped_column(ForeignKey('partners.id'))
  partner: Mapped['Partner'] = relationship(back_populates='bank_account')




class Partner(Base):
  __tablename__ = 'partners'
  
  title: Mapped[str]
  law_title: Mapped[str]
  price: Mapped[int]
  contract_number: Mapped[str] = mapped_column(nullable=True)
  service_name: Mapped[str]
  category: Mapped[PartnerCategory] = mapped_column(SQLEnum(PartnerCategory), default=PartnerCategory.OT)
  bank_account: Mapped[BankAccount] = relationship(back_populates='partner', cascade='all, delete-orphan')