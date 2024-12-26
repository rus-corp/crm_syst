from apps.base.base_handler import BaseHandler

from apps.base import exceptions
from .dal import PartnerDAL, BankAccountDAL
from . import schemas



class BankAccountHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.bank_dal = BankAccountDAL(self.session)
  
  async def _create_account(self, body: schemas.BankAccountBase) -> schemas.BankAccountShowBase:
    async with self.session.begin():
      body_data = body.model_dump()
      account = await self.bank_dal.create_account(values=body_data)
      return account
  
  
  async def _get_bank_account_by_id(self, account_id: int):
    account = await self.bank_dal.get_bank_account(account_id)
    return account
  
  
  async def _update_banck_account(self, account_id: int, values):...




class PartnerHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.partner_dal = PartnerDAL(self.session)
  
  
  async def _create_partner(self, body: schemas.PartnerBase):
    async with self.session.begin():
      body_data = body.model_dump()
      partner = await self.partner_dal.create_partner(values=body_data)
      return partner
  
  
  async def _get_all_partners(self, flag: bool = False):
    """if flag -> partner with bank"""
    if flag:
      partners = await self.partner_dal.get_partners_with_bank()
    else:
      partners = await self.partner_dal.get_all_partners()
    return list(partners)
  
  
  async def _get_partner_by_id(self, partner_id: int, flag: bool = False):
    """if flag -> partner with bank"""
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
  
  
  async def _create_partner_with_bank(self, body: schemas.CreatePartnerAndBank):
    async with self.session.begin():
      body_data = body.model_dump()
      bank_account = body_data.pop('bank_account', False)
      if not bank_account:
        raise exceptions.AppBaseExceptions.item_not_found(
          item_data='Bank Account'
        )
      partner_bank_handler = BankAccountHandler(self.session)
      partner_bank_acc = await partner_bank_handler._create_account(bank_account)
      if partner_bank_acc is None:
        raise exceptions.AppBaseExceptions.item_not_found(
          item_data='Bank Account'
        )
      body_data['bank_account_id'] = partner_bank_acc.id
      new_partner = await self.partner_dal.create_partner(
        values=body_data
      )
      return schemas.PartnerBankCreateResponse(
        id=new_partner.id,
        title=new_partner.title,
        law_title=new_partner.law_title,
        price=new_partner.price,
        contract_number=new_partner.contract_number,
        bank_account=partner_bank_acc
      )