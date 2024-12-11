from apps.base.base_dal import BaseDAL



from core.models.partners_models import Partner, BankAccount
from . import schemas




class PartnerDAL(BaseDAL):
  model = Partner
  
  async def create_partner(self, values: schemas.PartnerValues) -> schemas.PartnerBaseShow:
    result = await self.base_create_item(
      model=self.model,
      values=values,
      commit=True
    )
    return result
  
  
  async def get_all_partners(self):
    result = await self.base_get_all_items(self.model)
    return result
  
  
  async def get_one_partner(self, partner_id: int):
    result = await self.base_get_one_item(
      model=self.model,
      item_id=partner_id
    )
    return result
  
  
  async def update_partner_by_id(self, partner_id: int, values: dict):
    result = await self.base_update_item(
      model=self.model,
      item_id=partner_id,
      values=values
    )
    return result
  
  
  async def delete_partner(self, partner_id: int):
    result = await self.base_delete_item(
      model=self.model,
      item_id=partner_id
    )
    return result





class BankAccountDAL(BaseDAL):
  model = BankAccount
  
  async def create_account(self, values):
    result = await self.base_create_item(
      model=self.model,
      values=values
    )
    return result
  
  
  async def get_bank_account(self, account_id: int):
    result = await self.base_get_one_item(
      model=self.model,
      item_id=account_id
    )
    return result