from fastapi.responses import JSONResponse
from apps.base.base_handler import BaseHandler
from apps.base.exceptions import AppBaseExceptions
from ..dals.expenses_dal import ExpensesDAL
from apps.program_app.dals import ProgramDAL
from .. import schemas





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
