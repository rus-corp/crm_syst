from apps.base.base_handler import BaseHandler

from apps.base import exceptions
from .dal import PartnerDAL, BankAccountDAL, PartnerServicesDAL
from . import schemas



class BankAccountHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.bank_dal = BankAccountDAL(self.session)
  
  async def __create_account(self, body: dict) -> schemas.BankAccountShowBase:
    account = await self.bank_dal.create_account(values=body)
    return account
  
  
  async def _create_bank_with_partner(self, body: dict):
    bank_account = await self.__create_account(body=body)
    return bank_account
  
  
  async def _create_bank_item(self, body: schemas.BankAccountPartnerCreateRequest):
    async with self.session.begin():
      body_data = body.model_dump()
      bank_account = await self.__create_account(body=body_data)
      return bank_account
  
  
  async def _get_bank_account_by_id(self, account_id: int):
    account = await self.bank_dal.get_bank_account(account_id)
    return account
  
  
  async def _update_bank_account(self, account_id: int, values: schemas.BankAccountUpdateRequest):
    async with self.session.begin():
      body_data = values.model_dump(exclude_none=True)
      updated_account = await self.bank_dal.update_bank_account(
        account_id=account_id,
        values=body_data
      )
      return updated_account
  
  
  async def _delete_bank_account(self, account_id: int):
    async with self.session.begin():
      deleted_account = await self.bank_dal.delete_bank_account(account_id)
      return deleted_account




class PartnerServiceHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.partner_service_dal = PartnerServicesDAL(self.session)
  
  
  async def _create_partner_service(self, values: schemas.PartnerServiceCreateRequest):
    async with self.session.begin():
      body_data = values.model_dump()
      created_service = await self.partner_service_dal.create_service(body_data)
      return created_service
  
  
  async def _get_all_services(self):
    services_list = await self.partner_service_dal.get_all_services()
    return list(services_list)
  
  
  async def _get_service_item(self, service_id: int):
    service_item = await self.partner_service_dal.get_service_item(service_id)
    return service_item
  
  
  async def _update_partner_service(self, service_id: int, body: schemas.PartnerServiceUpdateRequest):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      updated_service = await self.partner_service_dal.update_service_by_id(
        service_id=service_id,
        values=body_data
      )
      return updated_service
  
  
  async def _delete_partner_service(self, service_id: int):
    async with self.session.begin():
      deleted_service = await self.partner_service_dal.delete_service(service_id)
      return deleted_service




class PartnerHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.partner_dal = PartnerDAL(self.session)
  
  
  async def _create_partner(self, body: schemas.PartnerBase):
    async with self.session.begin():
      body_data = body.model_dump()
      partner = await self.partner_dal.create_partner(values=body_data)
      return partner
  
  
  async def _get_all_partners(self, category: str):
    if category:
      partners = await self.partner_dal.get_filter_partner_list(category)
    else:
      partners = await self.partner_dal.get_all_partners()
    return list(partners)
  
  
  async def _get_partner_by_id(self, partner_id: int, flag: bool = False):
    """if flag -> partner with bank and service"""
    if flag:
      partner = await self.partner_dal.ger_partner_by_id_with_account(partner_id)
    else:
      partner = await self.partner_dal.get_one_partner(partner_id)
    return partner
  
  
  async def _update_partner(self, partner_id: int, body: schemas.PartnerUpdateRequest):
    async with self.session.begin():
      body_data = body.model_dump(exclude_none=True)
      updated_partner = await self.partner_dal.update_partner_by_id(
        partner_id=partner_id,
        values=body_data
      )
      return updated_partner
  
  
  
  async def _delete_partner_by_id(self, partner_id: int):
    async with self.session.begin():
      deleted_partner = await self.partner_dal.delete_partner(partner_id)
      return deleted_partner
  
  
  async def _create_partner_with_service(self, body: schemas.CreatePartnerAndServiceRequest):
    async with self.session.begin():
      body_data = body.model_dump()
      partner_services = body_data.pop('partner_services', False)
      if not partner_services:
        raise exceptions.AppBaseExceptions.item_not_found(
          item_data='Bank Account'
        )
      new_partner = await self.partner_dal.create_partner(
        values=body_data
      )
      for service in partner_services:
        service['partner_id'] = new_partner.id
      partner_service_dal = PartnerServicesDAL(self.session)
      created_partner_services = await partner_service_dal.create_many_services(partner_services)
      return schemas.CreatePartnerAndServiceResponse(
        id=new_partner.id,
        title=new_partner.title,
        law_title=new_partner.law_title,
        contract_number=new_partner.contract_number,
        category=new_partner.category,
        partner_services=created_partner_services
      )
  
  
  async def _get_partners_with_services(self):
    partner_list = await self.partner_dal.get_partners_with_services()
    return list(partner_list)
  
  
  async def _append_partner_to_program(
    self,
    body:list[schemas.AppendPartnerToProgramRequest]
  ):
    async with self.session.begin():
      service_dal = PartnerServicesDAL(self.session)
      # program_dal = PartnerDAL(self.session)
      created_data = []
      for item in body:
        body_data = item.model_dump()
        service_item = await service_dal.get_service_item(body_data['service_id'])
        if not service_item:
          raise exceptions.AppBaseExceptions.item_not_found(
            item_data='Service'
          )
        program_partner = await self.partner_dal.append_partner_service_to_program(
          partner_id=body_data['partner_id'],
          program_id=body_data['program_id'],
          service_id=body_data['service_id']
        )
        created_data.append(program_partner)
      return created_data