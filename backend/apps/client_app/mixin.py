from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from .client.dals import ClientDAL
from ..utils.slug import create_slug
from apps.payments_app.dals import PaymentDAL


class ClientMixin:
  def __init__(self, session: AsyncSession):
    self.session = session
    self.client_dal = ClientDAL(self.session)
    self.payment_dal = PaymentDAL(self.session)
  
  
  async def get_client_data(self, client_id: int):
    client = await self.client_dal.get_client_by_id(client_id)
    return client
  
  
  async def check_and_create_client_slug(self, client_data: dict):
    unique_slug = create_slug(client_data['name'] + client_data['last_name'])
    client = await self.client_dal.get_client_by_slug(unique_slug)
    if client:
      unique_slug = create_slug(
        client_data['name'] 
        + client_data['last_name'] 
        + client_data['second_name'] 
        + (datetime.now()).strftime('%Y-%m-%d').split(' ')[0]
      )
    return unique_slug
  
  
  async def get_client_program_price(self, program_client_id: int):
    client_program = await self.payment_dal.get_client_program_price(program_client_id)
    client_data = await self.client_dal.get_client_by_id_with_profile(client_program.client_id)
    return_data = {}
    if client_data.profile.status == 'New':
      return_data['price'] = client_program.program.prices.base_price
    elif client_data.profile.status == 'Regular' and client_data.profile.community:
      return_data['price'] = client_program.program.prices.comunity_price
    elif client_data.profile.status == 'Regular':
      return_data['price'] = client_program.program.prices.loayal_price
    return return_data
  
  
  async def save_program_price(self, program_client_id: int):
    client_program_price = await self.get_client_program_price(program_client_id)
    save_client_program_price = await self.payment_dal.update_program_clients_table(
      program_clients_id=program_client_id,
      values=client_program_price
    )
    return save_client_program_price
  
  
  # async def delete_client_price_after_check_out(self)