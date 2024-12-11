from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey


from ..database import Base




class BankAccount(Base):
  __tablename__ = 'bank_account'
  bank_name: Mapped[str]
  bic: Mapped[str]
  account_number: Mapped[str]
  cor_account: Mapped[str]




class Partner(Base):
  __tablename__ = 'partner'
  
  title: Mapped[str]
  law_title: Mapped[str]
  price: Mapped[int]
  contract_number: Mapped[str] = mapped_column(nullable=True)
  
  bank_account_id: Mapped[int] = mapped_column(ForeignKey('bank_account.id'))