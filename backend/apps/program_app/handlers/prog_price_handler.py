from apps.base.base_handler import BaseHandler
from ..dals.prog_price_dal import ProgramPriceDAL
from ..dals.program_dal import ProgramDAL



class ProgramPriceHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.price_dal = ProgramPriceDAL(self.session)
    self.program_dal = ProgramDAL(self.session)
  
  
  async def _create_program_price(self, program_slug: str):
    async with self.session.begin():
      program_expenses = await self.program_dal.get_program_expenses(program_slug)
      for expense in program_expenses.expenses:
        ...