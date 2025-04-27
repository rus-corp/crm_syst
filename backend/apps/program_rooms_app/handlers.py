from sqlalchemy.ext.asyncio import AsyncSession
from apps.base.base_handler import BaseHandler

from .dals import ProgramRoomDAL

class ProgramRoomsHandler(BaseHandler):
  def __init__(self, session: AsyncSession):
    super().__init__(session)
    self.program_room_dal = ProgramRoomDAL(self.session)
  
  
  async def _get_program_room_clients(self, program_room_id: int):
    program_room_clients = await self.program_room_dal.get_program_room_client(program_room_id)
    return list(program_room_clients)