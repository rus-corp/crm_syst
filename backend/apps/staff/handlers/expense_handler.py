from fastapi.responses import JSONResponse
from apps.base.base_handler import BaseHandler
from apps.base.exceptions import AppBaseExceptions
from ..dals.expenses_dal import ExpensesDAL
from apps.program_app.dals.program_dal import ProgramDAL
from .. import schemas





class ExpenseHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.expense_dal = ExpensesDAL(self.session)
  
  
  async def _create_expenses(self, body: schemas.ExpenseCreateRequst):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      expense_item = await self.expense_dal.get_or_create_expenses(values=body_data)
      return expense_item
  
  
  async def _get_all_expenses(self, expense_limit=None):
    if expense_limit:
      expeneses = await self.expense_dal.get_all_expenses(limit=expense_limit)
    else:
      expeneses = await self.expense_dal.get_all_expenses()
    return list(expeneses)
  
  
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
  
  
  async def _create_program_static_empl_expenses(self, body: schemas.StaticEmployeeExpenseCreateRequset):
    async with self.session.begin():
      program_dal = ProgramDAL(self.session)
      body_data = body.model_dump()
      employee_expense = body_data['employee_expense']
      employee_format_data = []
      for expense in employee_expense:
        for item in expense['expenses']:
          employee_format_data.append({
            'program_id': expense['program_id'],
            'employee_id': expense['employee_id'],
            'category': item['category'],
            'amount': item['amount']
          })
      all_expenses = body_data['static_expense'] + employee_format_data
      for expense in all_expenses:
        program_id = expense.pop('program_id')
        empl_expense = await self.expense_dal.get_or_create_expenses(expense)
        program_expense = await program_dal.get_program_for_append_expenses(
          program_id=program_id,
        )
        program_expense.expenses.append(empl_expense)
      await self.session.commit()
      return JSONResponse(
        content='Expense appended to program',
        status_code=201
      )
      