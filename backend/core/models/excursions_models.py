from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import Enum as SQLEnum


from ..database import Base


class Excursion(Base):
  __tablename__ = 'excursion'
  title: Mapped[str]
  desc: Mapped[str]
  price: Mapped[int]