from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest

from .test_data import (
  program_test_data,
  test_hotel_rooms,
  test_program_rooms,
  test_hotels,
  test_append_client_to_prog,
  test_append_client_to_prog_room,
  test_append_client_to_prog_room_bad
)
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
  progHot = await ac.get('/program/base/program_hotels/1')
  assert progHot.status_code == 200
  programHotels = progHot.json()
  for hotel in programHotels:
    hotelData = hote_schemas.HotelWithRooms(**hotel)
    assert hotelData.title == test_hotels[hotelData.id - 1]['title']





async def test_append_client_to_program(ac: AsyncClient):
  for item in test_append_client_to_prog[:-1]:
    req = await ac.post('/program/base/append_client/', json=item)
    assert req.status_code == 201
  # проверка на изменение программы, а не создания доп записи клиент - программа
  bad_req = await ac.post('/program/base/append_client/', json=test_append_client_to_prog[-1])
  assert bad_req.status_code == 201
  client_list_req = await ac.get('/clients/base/')
  assert client_list_req.status_code == 200
  client_list_data = client_list_req.json()
  current_client = None
  for cl in client_list_data:
    if cl['id'] == 1:
      current_client = cl
  client_cur_prog_req = await ac.get(f'/clients/base/program/{current_client['slug']}')
  assert client_cur_prog_req.status_code == 200
  client_cur_prog = client_cur_prog_req.json()
  assert client_cur_prog['program']['id'] == 3



async def test_append_client_to_program_room(ac: AsyncClient):
  for item in test_append_client_to_prog_room:
    req = await ac.post('/clients/base/append_client_to_prog_room', json=item)
    assert req.status_code == 201
  for item in test_append_client_to_prog_room_bad:
    req = await ac.post('/clients/base/append_client_to_prog_room', json=item)
    assert req.status_code == 403


# async def test_bad_append_cleint_to_room(ac: AsyncClient):...





# async def create_client_family(ac: AsyncClient)

# async def get_client_family(ac: AsyncClient):

# async def test_get_program_clients(ac: AsyncClient):...

# async def test_delete_client_to_program(ac: AsyncClient):...
