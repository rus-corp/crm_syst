from ...base.base_dal import BaseDAL
from sqlalchemy import update, insert

from core.models.hotels_models import HotelRooms

class HotelRoomsDAL(BaseDAL):
  model = HotelRooms
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
  
  
  async def create_many_rooms(self, values: list[dict]):
    stmt = insert(self.model).values(values).returning(self.model)
    result = await self.db_session.execute(stmt)
    await self.db_session.commit()
    return result.scalars().all()
  
  
  async def get_all_rooms(self):
    result = await self.base_get_all_items(model=self.model)
    return result
  
  
  async def get_room_by_id(self, hotel_room_id: int):
    result = await self.base_get_one_item(
      model=self.model,
      item_id=hotel_room_id
    )
    return result
  
  
  async def update_hotel_room(self, room_id: int, values):
    result = await self.base_update_item(
      model=self.model,
      item_id=room_id,
      values=values
    )
    return result
  
  
  async def delete_hotel_room(self, room_id: int):
    return await self.base_delete_item(HotelRooms, room_id)