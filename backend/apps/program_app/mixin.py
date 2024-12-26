from sqlalchemy.ext.asyncio import AsyncSession
from .dals.program_dal import ProgramDAL
from apps.staff.dals.expenses_dal import ExpensesDAL
from apps.staff.schemas import AppendExpensesToProgram
from apps.base.exceptions import AppBaseExceptions



class ProgramMixin:
  def __init__(self, session: AsyncSession):
    self.session = session
    self.program_dal = ProgramDAL(self.session)
  
  async def check_program_and_expenses(self, body: AppendExpensesToProgram):
    body_data = body.model_dump()
    program = await self.program_dal.get_program_for_append_expenses(body.program_id)
    if program is None:
      raise AppBaseExceptions.item_not_found(
        item_data='Program'
      )
    expense_dal = ExpensesDAL(self.session)
    expensive_item = await expense_dal.get_one_expense(body_data['expenses_id'])
    if expensive_item is None:
      raise AppBaseExceptions.item_not_found(
        item_data='Expenses'
      )
    return (program, expensive_item)