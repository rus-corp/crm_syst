from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy import Enum as SQLEnum

from ..database import Base
from .utils import EmployeePosition, StaticCategory, ExpenseType


if TYPE_CHECKING:
  from .program_models import Program



class Employee(Base):
  __tablename__ = 'employees'
  
  first_name: Mapped[str]
  last_name: Mapped[str]
  position: Mapped[EmployeePosition] = mapped_column(
    SQLEnum(EmployeePosition), default=EmployeePosition.AM
  )
  comment: Mapped[str] = mapped_column(nullable=True)
  expenses: Mapped[List['Expenses']] = relationship(
    back_populates='employee',
    lazy='joined'
  )




class Expenses(Base):
  __tablename__ = 'expenses'
  __table_args__ = (UniqueConstraint('category', 'amount', 'employee_id'), )
  
  amount: Mapped[int]
  category: Mapped[str] = mapped_column(SQLEnum(StaticCategory))
  employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'), nullable=True)
  expense_type: Mapped[ExpenseType] = mapped_column(SQLEnum(ExpenseType), default=ExpenseType.GR, nullable=True)
  employee: Mapped[Employee] = relationship(back_populates='expenses')
  programs: Mapped[List['Program']] = relationship(
    secondary='program_expenses',
    back_populates='expenses'
  )