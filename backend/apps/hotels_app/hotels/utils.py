from apps.program_app.schemas import ProgramResponseForAppendHotelAndRoom
from apps.hotels_app.hotels.schemas import HotelForAppendToProgramResponse
from apps.hotels_app.hotel_rooms.schemas import RoomForAppendToProgramResponse
from core.models.hotels_models import HotelRooms




def format_program_data(data):
  return ProgramResponseForAppendHotelAndRoom(
    id=data.id,
    title=data.title,
    place=data.place
  )


def format_hotel_data(data):
  return HotelForAppendToProgramResponse(
    id=data.id,
    title=data.title,
    city=data.city,
    contacts=data.contacts
  )


def format_room_data(data):
  return RoomForAppendToProgramResponse(
    id=data.id,
    room_type=data.room_type,
    room_volume=data.room_volume,
    room_price=data.room_price
  )



def get_hotel_rooms_volume(rooms: list[HotelRooms]):
  room_volume = 0
  for room in rooms:
    room_volume += room.room_volume
  return room_volume