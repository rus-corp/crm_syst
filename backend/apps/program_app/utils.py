from typing import List, Dict
from apps.program_app.schemas import ProgramResponseForAppendHoteAndRoom
from apps.hotels_app.hotels.schemas import HotelForAppendToProgramResponse
from apps.hotels_app.hotel_rooms.schemas import RoomForAppendToProgramResponse
from apps.hotels_app.hotels.schemas import HotelWithRooms
from apps.hotels_app.hotel_rooms.schemas import RoomForHotelResponse


def data_format(data: List[Dict]) -> List[HotelWithRooms]:
  hotels = {}
  
  for entry in data:
    hotel_id = entry.hotel.id
    hotel_info = entry.hotel
    room_info = entry.room
    if hotel_id not in hotels:
      hotels[hotel_id] = {
        "title": hotel_info.title,
        "address": hotel_info.address,
        "desc": hotel_info.desc,
        "email": hotel_info.email,
        "contacts": hotel_info.contacts,
        "city": hotel_info.city,
        "rooms": []
      }
    hotels[hotel_id]['rooms'].append(
      RoomForHotelResponse(
        id=room_info.id,
        room_price=room_info.room_price,
        room_type=room_info.room_type,
        room_volume=room_info.room_volume
      )
    )
  
  return hotels