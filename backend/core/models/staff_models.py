from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy import Enum as SQLEnum

from ..database import Base
from .utils import EmployeePosition, ExpenseCategory


if TYPE_CHECKING:
  from .program_models import Program


# class CostItem(Base):
#   __tablename__ = 'cost_items'
#   title: Mapped[str]




class Employee(Base):
  __tablename__ = 'employees'
  
  first_name: Mapped[str]
  last_name: Mapped[str]
  position: Mapped[EmployeePosition] = mapped_column(SQLEnum(EmployeePosition), default=EmployeePosition.AM)
  
  expenses: Mapped[List['Expenses']] = relationship(back_populates='employee')




class Expenses(Base):
  __tablename__ = 'expenses'
  __table_args__ = (UniqueConstraint('category', 'amount', 'employee_id'), )
  
  category: Mapped[ExpenseCategory] = mapped_column(SQLEnum(ExpenseCategory), default=ExpenseCategory.SR)
  amount: Mapped[int]
  employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'))
  
  employee: Mapped[Employee] = relationship(back_populates='expenses')
  programs: Mapped[List['Program']] = relationship(
    secondary='program_expenses',
    back_populates='expenses'
  )