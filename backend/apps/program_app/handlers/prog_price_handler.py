from apps.base.base_handler import BaseHandler
from ..dals.prog_price_dal import ProgramPriceDAL
from ..dals.program_dal import ProgramDAL
# from apps.staff.schemas import ExpenseFullResponse


from .. import schemas

class ProgramPriceHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.price_dal = ProgramPriceDAL(self.session)
    self.program_dal = ProgramDAL(self.session)
  
  
  async def _create_program_price(self, program_slug: str):
    async with self.session.begin():
      program_expenses = await self.program_dal.get_program_expenses(program_slug)
      program_total_exp = 0
      # for expense in program_expenses.expenses:
      #   expenseItem = ExpenseFullResponse(**expense)
      #   program_total_exp += expenseItem.amount
  
  
  
  async def _update_program_prices(self, program_price_id: int, values: schemas.ProgramPricesUpdateRequest):
    async with self.session.begin():
      body_data = values.model_dump(exclude_none=True)
      updated_price = await self.price_dal.update_program_price(
        program_price_id=program_price_id,
        values=body_data
      )
      return updated_price
  
  
  async def _delete_program_price(self, program_price_id: int):
    async with self.session.begin():
      deleted_price = await self.price_dal.delete_program_price(program_price_id)
      return deleted_price