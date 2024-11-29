from ...base.base_dal import BaseDAL
from sqlalchemy import update

from core.models.hotels_models import HotelRooms, Hotels

class HotelRoomsDAL(BaseDAL):
  async def create_room(
    self,
    room_type: str,
    room_price: int,
    room_volume: int,
    hotel_id: int
  ):
    new_room = HotelRooms(
      room_type=room_type,
      room_price=room_price,
      room_volume=room_volume,
      hotel_id=hotel_id,
    )
    self.db_session.add(new_room)
    await self.db_session.commit()
    return new_room
  
  
  async def get_all_rooms(self):
    return await self.base_get_all_items(HotelRooms)
  
  
  async def get_room_by_id(self, hotel_room_id: int):
    return await self.base_get_one_item(HotelRooms, hotel_room_id)
  
  
  async def update_hotel_room(self, room_id: int, values):
    query = update(HotelRoomsDAL).where(HotelRooms.id == room_id).values(**values).returning(HotelRooms)
    return await self.db_session.scalar(query)
  
  
  async def delete_hotel_room(self, room_id: int):
    return await self.base_delete_item(HotelRooms, room_id)