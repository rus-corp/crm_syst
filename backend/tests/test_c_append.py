from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest

from .test_data import test_program_expenses, program_test_data, test_hotel_rooms, test_program_rooms, test_hotels
from apps.base.base_schemas import BaseMessageResponseModel
from apps.hotels_app.hotels import schemas as hote_schemas





async def test_append_hotel_and_room_to_program(ac: AsyncClient):
  prRoom = await ac.post('/hotels/room_to_program/', json=test_program_rooms)
  assert prRoom.status_code == 201
  progRoomDAta = prRoom.json()
  for item in progRoomDAta:
    program_data = hote_schemas.ProgramHotelRoomResponse(**item)
    assert program_data.program.title == program_test_data[program_data.program.id - 1]['title']
    assert program_data.hotel.title == test_hotels[program_data.hotel.id - 1]['title']
    assert program_data.room.room_price == test_hotel_rooms[program_data.room.id - 1]['room_price']


async def test_get_program_rooms(ac: AsyncClient):
  progHot = await ac.get('/programs/program_hotels/1')
  assert progHot.status_code == 200
  programHotels = progHot.json()
  for hotel in programHotels:
    hotelData = hote_schemas.HotelWithRooms(**hotel)
    assert hotelData.title == test_hotels[hotelData.id - 1]['title']





# async def test_append_client_to_program(ac: AsyncClient):
#   programClient = await ac.post('/programs/append_client/')













# async def create_client_family(ac: AsyncClient)

# async def get_client_family(ac: AsyncClient):

# async def test_get_program_clients(ac: AsyncClient):...


# async def test_append_client_to_program(ac: AsyncClient):...

# async def test_delete_client_to_program(ac: AsyncClient):...

# async def test_append_hotel_to_program(ac: AsyncClient):...