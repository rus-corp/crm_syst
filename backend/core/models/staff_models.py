from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy import Enum as SQLEnum

from ..database import Base
from .utils import EmployeePosition


if TYPE_CHECKING:
  from .program_models import Program





class CostItem(Base):
  __tablename__ = 'cost_items'
  title: Mapped[str]
  expenses: Mapped[List['Expenses']] = relationship(back_populates='category')




class Employee(Base):
  __tablename__ = 'employees'
  
  first_name: Mapped[str]
  last_name: Mapped[str]
  position: Mapped[EmployeePosition] = mapped_column(SQLEnum(EmployeePosition), default=EmployeePosition.AM)
  
  expenses: Mapped[List['Expenses']] = relationship(back_populates='employee')




class Expenses(Base):
  __tablename__ = 'expenses'
  __table_args__ = (UniqueConstraint('category_id', 'amount', 'employee_id'), )
  
  amount: Mapped[int]
  category_id: Mapped[int] = mapped_column(ForeignKey('cost_items.id'), nullable=True)
  employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'), nullable=True)
  
  category: Mapped[CostItem] = relationship(back_populates='expenses', lazy='joined')
  employee: Mapped[Employee] = relationship(back_populates='expenses', lazy='joined')
  programs: Mapped[List['Program']] = relationship(
    secondary='program_expenses',
    back_populates='expenses'
  )