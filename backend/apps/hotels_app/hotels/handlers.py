from ...base.base_handler import BaseHandler
from ...base.exceptions import AppBaseExceptions
from fastapi.exceptions import HTTPException

from ...program_app.dals.program_dal import ProgramDAL
from ..hotel_rooms.dals import HotelRoomsDAL
from .dals import HotelDAL
from . import schemas
from core.models.hotels_models import HotelRooms
from .utils import format_program_data, format_hotel_data, format_room_data, get_hotel_rooms_volume





class HotelHandler(BaseHandler):
  def __init__(self, session):
    super().__init__(session)
    self.hotel_dal = HotelDAL(self.session)
  
  
  async def _create_hotel(self, hotel_body: schemas.CreateHotelRequest):
    async with self.session.begin():
      hotel_data = hotel_body.model_dump(exclude_none=True)
      created_hotel = await self.hotel_dal.create_hotel(**hotel_data)
      return schemas.HotelBaseResponse(
        id=created_hotel.id,
        title=created_hotel.title,
        address=created_hotel.address,
        contacts=created_hotel.contacts,
        city=created_hotel.city,
        email=created_hotel.email,
        des=created_hotel.desc
      )
  
  
  async def _get_all_hotels(self, flag: bool = False):
    """if flag - get hotel with rooms"""
    async with self.session.begin():
      if flag:
        hotels_list = []
        hotels = await self.hotel_dal.get_all_hotels_with_rooms()
        for hotel in hotels:
          rooms_volume = get_hotel_rooms_volume(hotel.rooms)
          hotels_list.append(
            schemas.HotelWithRooms(
              id=hotel.id,
              title=hotel.title,
              address=hotel.address,
              contacts=hotel.contacts,
              city=hotel.city,
              email=hotel.email,
              desc=hotel.desc,
              rooms=hotel.rooms,
              hotel_rooms_volume=rooms_volume
            )
          )
        return hotels_list
      else:
        hotels = await self.hotel_dal.get_all_hotels()
      return list(hotels)
  
  
  async def _get_one_hotel(self, hotel_id: int, flag: bool = False):
    """if flag - get hotel with rooms"""
    async with self.session.begin():
      if flag:
        hotel = await self.hotel_dal.get_hotel_item_with_rooms(hotel_id)
        room_volumes = get_hotel_rooms_volume(hotel.rooms)
        return schemas.HotelWithRooms(
          id=hotel.id,
          title=hotel.title,
          address=hotel.address,
          contacts=hotel.contacts,
          city=hotel.city,
          email=hotel.email,
          desc=hotel.desc,
          rooms=hotel.rooms,
          hotel_rooms_volume=room_volumes
        )
      else:
        hotel = await self.hotel_dal.get_hotel_by_id(hotel_id)
      return hotel
  
  
  async def _update_hotel(self, hotel_id: int, hotel_body: schemas.HotelUpdateRequest):
    async with self.session.begin():
      hotel_data = hotel_body.model_dump(exclude_none=True)
      updated_hotel = await self.hotel_dal.update_hotel(
        hotel_id=hotel_id,
        values=hotel_data
      )
      return updated_hotel
  
  
  async def _delete_hotel_by_id(self, hotel_id: int):
    async with self.session.begin():
      deleted_hotel = await self.hotel_dal.delete_hotel(hotel_id)
      return deleted_hotel
  
  
  async def _append_hotel_and_rooms_to_program(
    self,
    body: schemas.AppendHotelAndRoomToProgram
  ):
    async with self.session.begin():
      body_data = body.model_dump()
      rooms_dal = HotelRoomsDAL(self.session)
      room: HotelRooms = await rooms_dal.get_room_by_id(body_data['room_id'])
      if room.hotel_id != body_data['hotel_id']:
        raise AppBaseExceptions.relation_not_exsist(
          main_model='Hotel', main_item_id=body_data['hotel_id'],
          second_model='Rooms', second_item_id=body_data['room_id']
        )
      hotel = await self.hotel_dal.get_hotel_by_id(body_data['hotel_id'])
      program_dal = ProgramDAL(self.session)
      current_program = await program_dal.get_program_by_id(body_data['program_id'])
      if not current_program or not hotel or not room:
        raise AppBaseExceptions.item_not_found('Program or Hotel or Room')
      try:
        program_hotel_room = await self.hotel_dal.append_hotel_and_room_to_program(
          program=current_program,
          hotel=hotel,
          room=room
        )
        program_response = format_program_data(program_hotel_room.program)
        hotel_response = format_hotel_data(program_hotel_room.hotel)
        room_response = format_room_data(program_hotel_room.room)
        return schemas.ProgramHotelRoomResponse(
          program=program_response,
          hotel=hotel_response,
          room=room_response
        )
      except:
        await self.session.rollback()
  
  
  async def _delete_hotel_room_from_program(
    self,
    body: schemas.AppendHotelAndRoomToProgram
  ):
    async with self.session.begin():
      body_data = body.model_dump()
      deleted_room = await self.hotel_dal.delete_hotel_room_from_program(**body_data)
      if deleted_room is None:
        return AppBaseExceptions.relation_not_exsist(
          main_model='Program',
          main_item_id=body.program_id,
          second_model='Hotel Room',
          second_item_id=body.room_id
        )
      return deleted_room