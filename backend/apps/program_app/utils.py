from typing import List, Dict
from apps.hotels_app.hotel_rooms.schemas import RoomForHotelResponse
from apps.hotels_app.hotels.utils import get_hotel_rooms_volume
from .schemas import ProgramBaseResponse
from core.models.program_models import Program
from core.models.staff_models import Expenses


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
        "client_count": data.client_count,
    }
  if duration:
    common_data['duration'] = data.duration()
  return ProgramBaseResponse(**common_data)



def calculate_program_expenses(program_expenses: list[Expenses], program_client_base_count: int) -> int:
  total = 0
  for item in program_expenses:
    if item.expense_type == 'group':
      total += (item.amount / program_client_base_count)
    else:
      total += item.amount
  return int(total)



def calculate_program_partners(program_partners: list[dict], program_client_base_count: int) -> int:
  total = 0
  for partner in program_partners:
    partner_service = partner.service
    if partner_service.service_type == 'group':
      total += (partner_service.price / program_client_base_count)
    else:
      total += partner_service.price
  return int(total)