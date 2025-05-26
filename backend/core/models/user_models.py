from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy import Enum as SQLEnum

from ..database import Base
from .utils import UserRole



class User(Base):
  email: Mapped[str] = mapped_column(unique=True)
  first_name: Mapped[str]
  last_name: Mapped[str]
  password: Mapped[str]
  role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.MG)