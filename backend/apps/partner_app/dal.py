from apps.base.base_dal import BaseDAL
from sqlalchemy import select, delete, insert
from sqlalchemy.orm import joinedload, selectinload


from core.models.partners_models import Partner, BankAccount, PartnerService
from core.models.association_models import ProgramPartners




class PartnerDAL(BaseDAL):
  model = Partner
  
  async def create_partner(self, values: dict) -> Partner:
    result = await self.base_create_item(
      model=self.model,
      values=values,
    )
    return result
  
  
  async def get_all_partners(self):
    result = await self.base_get_all_items(self.model)
    return result
  
  
  async def get_filter_partner_list(self, category: str):
    query = (select(self.model)
             .where(self.model.category == category)
             .order_by(self.model.id)
             .options(joinedload(self.model.partner_services)))
    result = await self.db_session.execute(query)
    return result.scalars().unique().all()
  
  
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
    query = (select(self.model)
             .options(joinedload(self.model.bank_account))
             .order_by(self.model.id))
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def get_partners_with_services(self):
    query = select(self.model).options(joinedload(self.model.partner_services))
    result = await self.db_session.execute(query)
    return result.scalars().unique().all()
  
  
  async def ger_partner_by_id_with_account(self, partner_id: int):
    query = (select(self.model)
             .where(self.model.id == partner_id)
             .options(
               joinedload(self.model.bank_account),
               joinedload(self.model.partner_services)
             ))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def delete_partner(self, partner_id: int):
    result = await self.base_delete_item(
      model=self.model,
      item_id=partner_id
    )
    return result
  
  
  async def append_partner_service_to_program(
    self,
    program_id: int,
    partner_id: int,
    service_id: int
  ):
    stmt = ProgramPartners(
      program_id=program_id,
      partner_id=partner_id,
      service_id=service_id
    )
    self.db_session.add(stmt)
    await self.db_session.flush()
    return stmt
  
  
  async def delete_partner_service_from_program(
    self,
    program_id: int,
    partner_id: int,
    service_id: int
  ):
    stmt = delete(ProgramPartners).where(
      ProgramPartners.program_id == program_id,
      ProgramPartners.partner_id == partner_id,
      ProgramPartners.service_id == service_id
    ).returning(ProgramPartners.id)
    result = await self.db_session.execute(stmt)
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
  
  
  async def update_bank_account(self, account_id: int, values: dict):
    result = await self.base_update_item(
      model=self.model,
      item_id=account_id,
      values=values
    )
    return result
  
  
  async def delete_bank_account(self, account_id: int):
    result = await self.base_delete_item(
      model=self.model,
      item_id=account_id
    )
    return result



class PartnerServicesDAL(BaseDAL):
  model = PartnerService
  
  async def create_service(self, values):
    result = await self.base_create_item(
      model=self.model,
      values=values
    )
    return result
  
  
  async def create_many_services(self, services: list[dict]):
    stmt = insert(self.model).values(services).returning(self.model)
    result = await self.db_session.execute(stmt)
    await self.db_session.commit()
    return result.scalars().all()
  
  
  async def get_all_services(self):
    result = await self.base_get_all_items(self.model)
    return result
  
  
  async def get_service_item(self, service_id: int):
    result = await self.base_get_one_item(
      model=self.model,
      item_id=service_id
    )
    return result
  
  
  async def update_service_by_id(self, service_id: int, values: dict):
    result = await self.base_update_item(
      model=self.model,
      item_id=service_id,
      values=values
    )
    return result
  
  
  async def delete_service(self, service_id: int):
    result = await self.base_delete_item(
      model=self.model,
      item_id=service_id
    )
    return result