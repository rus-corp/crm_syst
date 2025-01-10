from ...base.base_handler import BaseHandler
from . import schemas
from .dals import HotelRoomsDAL



class HotelRoomsHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.room_dal = HotelRoomsDAL(self.session)
  
  
  async def _create_hotel_room(self, room_body: schemas.HoteRoomCreateRequset):
    async with self.session.begin():
      room_data = room_body.model_dump()
      new_room = await self.room_dal.create_room(**room_data)
      return new_room
  
  
  async def _create_many_hotel_rooms(self, rooms: list[schemas.HoteRoomCreateRequset]):
    async with self.session.begin():
      createRooms = []
      for room in rooms:
        body_data = room.model_dump()
        createRooms.append(body_data)
      createdRooms = await self.room_dal.create_many_rooms(createRooms)
      return createdRooms
  
  
  async def _get_all_rooms(self):
    async with self.session.begin():
      rooms = await self.room_dal.get_all_rooms()
      return list(rooms)
  
  
  async def _get_room_item(self, room_id: int):
    async with self.session.begin():
      room = await self.room_dal.get_room_by_id(room_id)
      return room
  
  
  async def _update_room(self, room_id: int, room_body: schemas.HotelRoomUpdateRequest):
    async with self.session.begin():
      room_data = room_body.model_dump(exclude_none=True)
      updated_room = await self.room_dal.update_hotel_room(
        room_id=room_id,
        values=room_data
      )
      return updated_room
  
  
  async def _delete_room_by_id(self, room_id: int):
    async with self.session.begin():
      deleted_room = await self.room_dal.delete_hotel_room(room_id)
      return deleted_room