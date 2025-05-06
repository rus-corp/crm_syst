from typing import Optional
from ..base.base_dal import BaseDAL
from sqlalchemy import select, delete
from sqlalchemy.orm import joinedload, selectinload
from core.models.association_models import ProgramClientRoom, ProgramClients, ProgramRooms
from datetime import date


class ProgramRoomDAL(BaseDAL):
  
  async def get_program_room_client(
    self,
    program_room_id: int
  ):
    query = (select(ProgramClientRoom)
             .where(
               ProgramClientRoom.program_room_id == program_room_id
             )
             .options(
               joinedload(ProgramClientRoom.program_clients)
               .joinedload(ProgramClients.client),
               joinedload(ProgramClientRoom.program_room)
               .joinedload(ProgramRooms.room)
             ))
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  
  async def append_client_to_program_room(
    self,
    program_client_id: int,
    program_room_id: int,
    entry_date: date,
    departue_date: date,
    no_sharing: bool,
    comment: Optional[str] = None
  ):
    new_client_room = ProgramClientRoom(
      program_client_id=program_client_id,
      program_room_id=program_room_id,
      entry_date=entry_date,
      departue_date=departue_date,
      no_sharing=no_sharing,
      comment=comment,
    )
    self.db_session.add(new_client_room)
    await self.db_session.flush()
    return new_client_room
  
  
  async def get_all_program_hotel_rooms(self):pass
  
  
  async def update_program_hotel_rooms(self):pass
  
  
  async def delete_program_hotel_rooms(self):pass
