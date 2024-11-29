from ...base.base_dal import BaseDAL
from sqlalchemy import select, update, delete, insert
from sqlalchemy.orm import selectinload, joinedload


from core.models.hotels_models import Hotels
from core.models.association_models import ProgramRooms


class HotelDAL(BaseDAL):
  async def create_hotel(
    self,
    title: str,
    address: str,
    contacts: str,
    city: str,
    email: str,
    desc: str = None,
  ) -> Hotels:
    new_hotel = Hotels(
      title=title,
      address=address,
      contacts=contacts,
      city=city,
      email=email,
      desc=desc
    )
    self.db_session.add(new_hotel)
    await self.db_session.commit()
    return new_hotel
  
  
  async def get_all_hotels(self) -> list[Hotels]:
    return await self.base_get_all_items(Hotels)
  
  
  async def get_hotel_by_id(self, hotel_id: int) -> Hotels:
    query = select(Hotels).where(Hotels.id == hotel_id)
    return await self.db_session.scalar(query)
  
  
  async def get_all_hotels_with_rooms(self):
    query = select(Hotels).options(joinedload(Hotels.rooms)).order_by(Hotels.id)
    result = await self.db_session.execute(query)
    return result.scalars().unique().all()
  
  
  async def get_hotel_item_with_rooms(self, hotel_id: int):
    query = select(Hotels).where(Hotels.id == hotel_id).options(joinedload(Hotels.rooms))
    return await self.db_session.scalar(query)
  
  
  async def update_hotel(self, hotel_id, values):
    query = update(Hotels).where(Hotels.id == hotel_id).values(**values).returning(Hotels)
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def delete_hotel(self, hotel_id):
    return await self.base_delete_item(Hotels, hotel_id)
  
  
  async def append_hotel_and_room_to_program(
    self,
    program,
    hotel,
    room
  ):
    program_hotel_rooms = ProgramRooms(
      program=program,
      hotel=hotel,
      room=room
    )
    self.db_session.add(program_hotel_rooms)
    await self.db_session.commit()
    return program_hotel_rooms