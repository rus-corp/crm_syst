from apps.base.base_handler import BaseHandler


from .dal import ClientProfileDAL
from . import schemas
from apps.base.exceptions import AppBaseExceptions
from ..mixin import ClientMixin
from apps.base.exceptions import AppBaseExceptions





class ClientProfileHandler(ClientMixin, BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.profile_dal = ClientProfileDAL(self.session)
  
  
  async def _create_client_profile(self, values:schemas.ProfileCreateRequest):
    async with self.session.begin():
      body_data = values.model_dump(exclude_none=True)
      has_client = await self.get_client_data(body_data['client_id'])
      if has_client is None:
        return AppBaseExceptions.item_not_found(item_data='Client')
      created_profile = await self.profile_dal.create_profile(body_data)
      if created_profile is None:
        raise AppBaseExceptions.item_not_found(item_data='Client')
      return created_profile
  
  
  async def _get_client_profile(self, client_id: int):
    client_profile = await self.profile_dal.get_client_profile(client_id)
    return client_profile
  
  
  async def _update_client_profile(self, client_id: int, values: schemas.ProfileUpdateRequest):
    async with self.session.begin():
      updated_profile = await self.profile_dal.update_client_profile(
        client_id=client_id,
        values=values
      )
      return updated_profile