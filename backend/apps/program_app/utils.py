from typing import List, Dict
from apps.hotels_app.hotel_rooms.schemas import RoomForHotelResponse
from apps.hotels_app.hotels.utils import get_hotel_rooms_volume
from .schemas import ProgramBaseResponse
from core.models.program_models import Program

def data_format(data: List[Dict]) -> Dict:
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



def program_response_format(data: Program, duration: bool = False) -> ProgramBaseResponse:
  common_data = {
        "id": data.id,
        "title": data.title,
        "start_date": data.start_date,
        "end_date": data.end_date,
        "place": data.place,
        "status": data.status,
        "desc": data.desc,
        "slug": data.slug,
    }
  if duration:
    common_data['duration'] = data.duration()
  return ProgramBaseResponse(**common_data)