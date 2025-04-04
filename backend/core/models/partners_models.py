from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey


from ..database import Base

from .utils import PartnerCategory
from .association_models import ProgramPartners



class PartnerService(Base):
  __tablename__ = 'partner_services'
  service_name: Mapped[str]
  price: Mapped[int]
  
  partner_id: Mapped[int] = mapped_column(ForeignKey('partners.id'))
  partner: Mapped['Partner'] = relationship(back_populates='partner_services')
  program_partner: Mapped[list[ProgramPartners]] = relationship(back_populates='service')



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
  contract_number: Mapped[str] = mapped_column(nullable=True)
  category: Mapped[PartnerCategory] = mapped_column(SQLEnum(PartnerCategory), default=PartnerCategory.OT)
  
  bank_account: Mapped[BankAccount] = relationship(back_populates='partner', cascade='all, delete-orphan')
  partner_services: Mapped[List[PartnerService]] = relationship(back_populates='partner', cascade='all, delete-orphan')
  
  program_partner: Mapped[list['ProgramPartners']] = relationship(back_populates='partner')