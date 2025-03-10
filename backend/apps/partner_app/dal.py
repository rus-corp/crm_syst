from apps.base.base_dal import BaseDAL
from sqlalchemy import select
from sqlalchemy.orm import joinedload


from core.models.partners_models import Partner, BankAccount
from . import schemas




class PartnerDAL(BaseDAL):
  model = Partner
  
  async def create_partner(self, values: dict) -> Partner:
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
  
  
  async def get_partners_with_bank(self):
    query = select(Partner).options(joinedload(Partner.bank_account)).order_by(Partner.id)
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def ger_partner_by_id_with_account(self, partner_id: int):
    query = select(Partner).where(Partner.id == partner_id).options(joinedload(Partner.bank_account))
    result = await self.db_session.execute(query)
    return result.scalar()





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
  
  
  async def update_bank_account(self, account_id: int, values: dict):...
  
  async def delete_bank_account(self, account_id: int):...