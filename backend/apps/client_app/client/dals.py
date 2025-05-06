from typing import Optional
from sqlalchemy.orm import selectinload, joinedload, contains_eager
from sqlalchemy import select, update, delete, and_, or_
from datetime import date

from ...base.base_dal import BaseDAL

from core.models.association_models import ProgramClients, ProgramClientRoom
from core.models.client_models import Client
from core.models.program_models import Program
from core.models.utils import ProgramStatus



class ClientDAL(BaseDAL):
  model = Client
  
  async def create_client(
    self,
    name:(str),
    last_name:(str),
    second_name:(str),
    phone:(str),
    email:(str),
    slug:(str)
  ):
    new_client = Client(
      name=name,
      last_name=last_name,
      second_name=second_name,
      phone=phone,
      email=email,
      slug=slug,
    )
    self.db_session.add(new_client)
    await self.db_session.flush()
    return new_client
  
  
  async def get_clients(self):
    return await self.base_get_all_items(model=self.model)
  
  
  async def get_client_by_id(self, client_id: int):
    query = select(Client).where(Client.id == client_id)
    result = await self.db_session.scalar(query)
    return result
  
  
  async def get_client_by_id_with_profile(self, client_id: int):
    query = select(Client).where(Client.id == client_id).options(joinedload(Client.profile))
    return await self.db_session.scalar(query)
  
  
  async def get_client_by_slug(self, client_slug: str):
    query = select(Client).where(Client.slug == client_slug).options(joinedload(Client.profile), joinedload(Client.document), joinedload(Client.client_family))
    result = await self.db_session.scalar(query)
    return result
  
  
  async def get_client_current_program(self, client_slug: str):
    query = (select(ProgramClients)
             .join(Client, ProgramClients.client_id == Client.id)
             .options(joinedload(ProgramClients.program))
             .where(Client.slug == client_slug)
             .where(ProgramClients.program.has(Program.status == ProgramStatus.AC)))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_client_current_program_with_profile_and_doc(self, client_slug: str):
    query = (select(Client)
             .where(Client.slug == client_slug)
             .options(
               selectinload(Client.client_program_detail)
               .selectinload(ProgramClients.program),
               joinedload(Client.profile),
               joinedload(Client.document)
             ))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_client_profile_and_doc(self, client_slug: str):
    query = (select(Client)
             .where(Client.slug == client_slug)
             .options(
               joinedload(Client.profile),
               joinedload(Client.document)
             ))
    result = await self.db_session.scalar(query)
    return result
  
  
  async def get_get_client_profile_and_doc_with_family(self, client_slug: str):
    query = (select(Client)
             .where(Client.slug == client_slug)
             .options(
               joinedload(Client.profile),
               joinedload(Client.document),
               joinedload(Client.client_family)
             ))
    result = await self.db_session.scalar(query)
    return result
  
  
  async def update_client_by_id(self, client_id, values):
    query = update(Client).where(Client.id == client_id).values(**values).returning(Client)
    result = await self.db_session.scalar(query)
  
  
  async def get_or_create_client(self, values):
    result = await self.base_get_or_create(
      model=self.model,
      values=values
    )
    return result
  
  
  async def get_program_room_all_clients(self, program_room_id: int, entry_date: date, departue_date: date):
    query = select(ProgramClientRoom).where(ProgramClientRoom.program_room_id == program_room_id)
#     stmt = select(ProgramClientRoom).where(
#     ProgramClientRoom.program_room_id == program_room_id,
#     or_(
#         and_(
#             ProgramClientRoom.entry_date <= entry_date,
#             ProgramClientRoom.departue_date > entry_date
#         ),
#         and_(
#             ProgramClientRoom.entry_date < entry_date,
#             ProgramClientRoom.departue_date >= departue_date
#         ),
#         and_(
#             ProgramClientRoom.entry_date >= entry_date,
#             ProgramClientRoom.departue_date <= departue_date
#         )
#     )
# )

    """
    првоерить что дата вьезда клиента меньше 
    """