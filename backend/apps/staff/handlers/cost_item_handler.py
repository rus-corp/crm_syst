from apps.base.base_handler import BaseHandler

from ..dals.cost_item_dal import CostItemDAL

from .. import schemas




class CostItemHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.cost_dal = CostItemDAL(self.session)
  
  
  async def _create_cost_item(self, values: schemas.CostItemBase):
    async with self.session.begin():
      body_data = values.model_dump()
      cost_item = await self.cost_dal.get_or_create_item(body_data)
      return cost_item
  
  
  async def _get_cost_item(self, cost_item_id: int):
    cost_item = await self.cost_dal.get_cost_item(cost_item_id)
    return cost_item
  
  
  async def _update_cost_item(self, cost_item_id: int, cost_body: schemas.CostItemBase):
    body_data = cost_body.model_dump()
    updated_item = await self.cost_dal.update_cost_items(
      cost_id=cost_item_id,
      values=body_data
    )
    return updated_item
  
  
  async  def _delete_cost_item(self, cost_item_id: int):
    delete_item = await self.cost_dal.delete_cost_item(cost_item_id)
    return delete_item