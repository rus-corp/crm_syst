from apps.program_app.schemas import ProgramResponseForAppendHoteAndRoom
from apps.hotels_app.hotels.schemas import HotelForAppendToProgramResponse
from apps.hotels_app.hotel_rooms.schemas import RoomForAppendToProgramResponse





def format_program_data(data):
  return ProgramResponseForAppendHoteAndRoom(
    id=data.id,
    title=data.title,
    place=data.place,
    price=data.price
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