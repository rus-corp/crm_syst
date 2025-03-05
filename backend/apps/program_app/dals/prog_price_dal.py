from apps.base.base_dal import BaseDAL
from core.models.program_models import ProgramPrices


class ProgramPriceDAL(BaseDAL):
  model = ProgramPrices
  
  async def create_program_price(self, values: dict):
    result = await self.base_create_item(
      model=self.model,
      values=values
    )
    return result
  
  
  async def update_program_price(self, program_price_id: int, values: dict):
    result = await self.base_update_item(
      model=self.model,
      item_id=program_price_id,
      values=values
    )
    return result
  
  
  async def delete_program_price(self, program_price_id: int):
    result = await self.base_delete_item(
      model=self.model,
      item_id=program_price_id
    )
    return result


