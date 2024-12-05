from sqlalchemy.orm import selectinload, joinedload, contains_eager
from sqlalchemy import select, update, delete, and_


from ..base.base_dal import BaseDAL

from core.models.association_models import ProgramClients
from core.models.client_models import Client
from core.models.program_models import Program
from core.models.utils import ProgramStatus



class ClientDAL(BaseDAL):
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
    await self.db_session.commit()
    return new_client
  
  
  async def get_clients(self):
    return await self.base_get_all_items(Client)
  
  
  async def get_client_by_id(self, client_id):
    query = select(Client).where(Client.id == client_id)
    result = await self.db_session.scalar(query)
    return result
  
  
  async def get_client_by_slug(self, client_slug: str):
    query = select(Client).where(Client.slug == client_slug).options(joinedload(Client.profile), joinedload(Client.document), joinedload(Client.client_family))
    result = await self.db_session.scalar(query)
    return result
  
  
  async def get_client_current_program(self, client_slug):
    query = (select(ProgramClients)
             .join(Client, ProgramClients.client_id == Client.id)
             .options(joinedload(ProgramClients.program))
             .where(Client.slug == client_slug)
             .where(ProgramClients.program.has(Program.status == ProgramStatus.AC)))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def update_client_by_id(self, client_id, values):
    query = update(Client).where(Client.id == client_id).values(**values).returning(Client)
    result = await self.db_session.scalar(query)
  
  
  async def append_client_to_room(self):pass