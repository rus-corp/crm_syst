from fastapi.responses import JSONResponse


from apps.base.base_handler import BaseHandler
from apps.base.exceptions import AppBaseExceptions

from .dals import ExpensesDAL, EmployeeDAL
from . import schemas
from apps.program_app.dals import ProgramDAL


class ExpenseHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.expense_dal = ExpensesDAL(self.session)
  
  
  async def _create_expenses(self, body: schemas.ExpenseCreateRequst):
    async with self.session.begin():
      body_data = body.model_dump()
      expense_item = await self.expense_dal.get_or_create_expenses(values=body_data)
      return expense_item
  
  
  async def _get_expense_by_id(self, expenses_id: int):
    expense_item = await self.expense_dal.get_one_expense(expenses_id)
    return expense_item
  
  async def _get_expense_with_employee(self, expenses_id: int):
    expense_item = await self.expense_dal.get_expenses_with_employee(expenses_id)
    return expense_item
  
  async def _update_expense_by_id(self, expenses_id: int, body: schemas.ExpensesUpdateRequest):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      expense_item = await self.expense_dal.update_expense(
        expense_id=expenses_id,
        values=body_data
      )
      return expense_item
  
  
  async def _delete_expense_by_id(self, expenses_id: int):
    async with self.session.begin():
      expense_item = await self.expense_dal.delete_expense(expenses_id)
      return expense_item
  
  
  async def _append_expensive_to_program(self, body: schemas.AppendExpensesToProgram):
    async with self.session.begin():
      body_data = body.model_dump()
      program_dal = ProgramDAL(self.session)
      program = await program_dal.get_program_for_append_expenses(body_data['program_id'])
      if program is None:
        raise AppBaseExceptions.item_not_found(
          item_data='Program'
        )
      expensive_item = await self.expense_dal.get_one_expense(body_data['expenses_id'])
      if expensive_item is None:
        raise AppBaseExceptions.item_not_found(
          item_data='Expenses'
        )
      program.expenses.append(expensive_item)
      return JSONResponse(content='Expenses added to Program', status_code=200)
  
  
  async def _delete_expensive_from_program(self):...
  
  
  async def _get_program_all_expensives(self, program_id: int):
    program_dal = ProgramDAL(self.session)
    program = await program_dal.get_program_for_append_expenses(program_id)
    return program




class EmployeeHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.employee_dal = EmployeeDAL(self.session)
  
  
  async def _create_employee(self, body: schemas.CreateEmployeeRequest):
    async with self.session.begin():
      body_data = body.model_dump()
      employee = await self.employee_dal.get_or_create_employee(body_data)
      return employee
  
  
  async def _get_all_employees(self):
    employees = await self.employee_dal.get_all_employees()
    return list(employees)
  
  
  async def _get_employee(self, employee_id: int):
    employee = await self.employee_dal.get_one_employee(employee_id)
    return employee
  
  
  async def _get_all_employees_with_expenses(self):
    employees = await self.employee_dal.get_all_employees_with_expenses()
    return list(employees)
  
  
  async def _get_employee_with_expenses(self, employee_id: int):
    employee = await self.employee_dal.get_employee_by_id_with_expenses(employee_id)
    return employee
  
  
  async def _update_employee(self, employee_id: int, body: schemas.EmployeeUpdateRequest):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      updated_employee = await self.employee_dal.update_employee(
        employee_id=employee_id,
        values=body_data
      )
      return updated_employee
  
  
  async def _delete_employee(self, employee_id: int):
    async with self.session.begin():
      deleted_employee = await self.employee_dal.delete_employee(employee_id)
      return deleted_employee
  
  
  async def _create_employee_and_expenses(self, body: schemas.CreateEmployeeWithExpensesRequest):
    async with self.session.begin():
      body_data = body.model_dump()
      expenses_data = body_data.pop('expenses', [])
      employee_item: schemas.EmployeeResponse = await self.employee_dal.get_or_create_employee(body_data)
      if employee_item is None:
        raise AppBaseExceptions.item_create_error(item_data='Employee')
      if not expenses_data:
        raise AppBaseExceptions.need_data(item_data='Expenses')
      expenses_dal = ExpensesDAL(self.session)
      for item in expenses_data:
        item['employee_id'] = employee_item['id']
      expenses_items: list[schemas.ExpenseBaseResponse] = await expenses_dal.create_many_items(expenses_data)
      return schemas.CreateEmployeeWithExpensesResponse(
        id=employee_item.id,
        first_name=employee_item.first_name,
        last_name=employee_item.last_name,
        position=employee_item.position,
        expenses=[expenses_items]
      )