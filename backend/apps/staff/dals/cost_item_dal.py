from apps.base.base_dal import BaseDAL
from core.models.staff_models import CostItem



class CostItemDAL(BaseDAL):
  model = CostItem
  
  async def get_or_create_item(self, values: dict):
    result = await self.base_get_or_create(
      model=self.model,
      values=values
    )
    return result
  
  
  async def get_all_cost_items(self):
    result = await self.base_get_all_items(
      model=self.model
    )
    return result
  
  async def get_cost_item(self, cost_id: int):
    result = await self.base_get_one_item(
      model=self.model,
      item_id=cost_id
    )
    return result
  
  
  async def update_cost_items(self, cost_id: int, values: dict):
    result = await self.base_update_item(
      model=self.model,
      item_id=cost_id,
      values=values
    )
    return result
  
  
  async def delete_cost_item(self, cost_id: int):
    result = await self.base_delete_item(
      model=self.model,
      item_id=cost_id
    )
    return result