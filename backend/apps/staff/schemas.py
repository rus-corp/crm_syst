from typing import List, Optional
from pydantic import BaseModel, ConfigDict


from core.models.utils import EmployeePosition, ExpenseCategory




class ExpensesBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  category: ExpenseCategory
  amount: int
  employee_id: int


class ExpenseCreateRequst(ExpensesBase):
  pass


class ExpenseBaseResponse(ExpensesBase):
  id: int


class ExpensesUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  category: Optional[ExpenseCategory] = None
  amount: Optional[int] = None
  employee_id: Optional[int] = None




class EmployeeBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  first_name: str
  last_name: str
  position: EmployeePosition


class CreateEmployeeRequest(EmployeeBase):
  pass


class EmployeeResponse(EmployeeBase):
  id: int


class EmployeeWithExpensesResponse(EmployeeResponse):
  expenses: Optional[List[ExpenseBaseResponse]] = []


class EmployeeUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  first_name: Optional[str] = None
  last_name: Optional[str] = None
  position: Optional[EmployeePosition] = None



class ExpensesWithEmployee(ExpenseBaseResponse):
  employee: EmployeeResponse


class AppendExpensesToProgram(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  program_id: int
  expenses_id: int



class CreateEmployeeWithExpensesRequest(CreateEmployeeRequest):
  expenses: Optional[List[ExpenseCreateRequst]] = None


class CreateEmployeeWithExpensesResponse(EmployeeResponse):
  expenses: Optional[List[ExpenseBaseResponse]] = None