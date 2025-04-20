from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest

from .test_data import (
  program_test_data,
  test_clients_data,
  test_client_details,
  test_client_documents,
  test_hotels,
  test_hotel_rooms,
  test_client_with_profile,
  test_client_prof_doc
)
from apps.program_app import schemas
from apps.client_app.client_profile.schemas import ProfileResponse
from apps.client_app.client_doc.schemas import DocumentResponse
from apps.client_app import schemas as client_schema
from apps.hotels_app.hotels import schemas as hotel_schema
from apps.hotels_app.hotel_rooms import schemas as room_schema



async def test_create_program(ac: AsyncClient):
  for item in program_test_data:
    prog = await ac.post('/program/base/', json=item)
    assert prog.status_code == 201
  program_db = await ac.get('/program/base/')
  assert program_db.status_code == 200
  program_data = program_db.json()
  assert len(program_data) == len(program_test_data)
  for prog in program_data:
    program = schemas.ProgramBaseResponse(**prog)
    assert program.id == prog['id']
  for i in program_data:
    id = i['id']
    assert i['title'] == program_test_data[id - 1]['title']



async def test_get_one_program(ac: AsyncClient):
  programs_list = await ac.get('/program/base/')
  assert programs_list.status_code == 200
  programs_list_data = programs_list.json()
  program_slug = programs_list_data[0]['slug']
  programItem = await ac.get(f'/program/base/{program_slug}')
  assert programItem.status_code == 200
  programItemData = programItem.json()
  program = schemas.ProgramBaseResponse(**programItemData)
  assert program.id == programs_list_data[0]['id']
  assert program.title == programs_list_data[0]['title']





async def test_create_clients(ac: AsyncClient):
  for item in test_clients_data:
    client = await ac.post('/clients/base/', json=item)
    assert client.status_code == 201
  
  client_db = await ac.get('/clients/base/')
  assert client_db.status_code == 200
  client_db_data = client_db.json()
  assert len(client_db_data) == len(test_clients_data)
  for cli in client_db_data:
    id = cli['id']
    assert cli['last_name'] == test_clients_data[id - 1]['last_name']
    assert cli['name'] == test_clients_data[id - 1]['name']




async def test_create_client_profile(ac: AsyncClient):
  for item in test_client_details[:-1]:
    client_profile = await ac.post('/clients/profile/', json=item)
    assert client_profile.status_code == 201
    profile_data = client_profile.json()
    profile = ProfileResponse(**profile_data)
    assert profile.shirt_size == item['shirt_size']
    assert profile.city == item['city']
  bad_req = await ac.post('/clients/profile/', json=test_client_details[-1])
  assert bad_req.status_code == 404


async def test_create_client_doc(ac: AsyncClient):
  for item in test_client_documents[:-1]:
    doc = await ac.post('/clients/doc/', json=item)
    assert doc.status_code == 201
    doc_data = doc.json()
    docum = DocumentResponse(**doc_data)
    assert docum.doc_type == item['doc_type']
    assert docum.series == item['series']
    assert docum.number == item['number']
  bad_req = await ac.post('/clients/doc/', json=test_client_documents[-1])
  assert bad_req.status_code == 404



async def test_list_items(ac: AsyncClient):
  client_req = await ac.get('/clients/base/')
  assert client_req.status_code == 200
  client_data = client_req.json()
  for item in client_data:
    id = item['id']
    client = client_schema.BaseShowClient(**item)
    client.name == test_clients_data[id - 1]['name']
    client.last_name == test_clients_data[id - 1]['last_name']


async def test_create_hotel(ac: AsyncClient):
  for item in test_hotels:
    hotel = await ac.post('/hotels/', json=item)
    assert hotel.status_code == 201
    hotel_data = hotel.json()
    hotelItem = hotel_schema.HotelBaseResponse(**hotel_data)
    assert hotelItem.title == item['title']
    assert hotelItem.city == item['city']


async def test_get_all_hotels(ac: AsyncClient):
  hotels = await ac.get('/hotels/')
  assert hotels.status_code == 200
  hotel_data = hotels.json()
  assert len(hotel_data) == len(test_hotels)
  for item in hotel_data:
    id = item['id']
    assert item['title'] == test_hotels[id - 1]['title']
    assert item['city'] == test_hotels[id - 1]['city']


async def test_get_hotel_item(ac: AsyncClient):
  hotel = await ac.get('/hotels/1')
  assert hotel.status_code == 200
  hotel_data = hotel.json()
  hotelItem = hotel_schema.HotelBaseResponse(**hotel_data)
  assert hotelItem.title == test_hotels[0]['title']
  assert hotelItem.city == test_hotels[0]['city']





async def test_create_hotel_rooom(ac: AsyncClient):
  for item in test_hotel_rooms:
    rooms = await ac.post('/rooms/', json=item)
    assert rooms.status_code == 201
    room_data = rooms.json()
    room = room_schema.HotelRoomBaseResponse(**room_data)
    assert room.room_type == item['room_type']
    assert room.hotel_id == item['hotel_id']
  rooms_data = await ac.get('/rooms/')
  assert rooms_data.status_code == 200
  rooms_data_js = rooms_data.json()
  assert len(rooms_data_js) == len(test_hotel_rooms)
  for room_item in rooms_data_js:
    roomItem = room_schema.HotelRoomBaseResponse(**room_item)
    id = roomItem.id
    assert roomItem.room_type == test_hotel_rooms[id - 1]['room_type']
    assert roomItem.room_price == test_hotel_rooms[id - 1]['room_price']
    assert roomItem.room_volume == test_hotel_rooms[id - 1]['room_volume']


async def test_create_client_with_profile(ac: AsyncClient):
  for item in test_client_with_profile:
    client_prof = await ac.post('/clients/base/client_profile', json=item)
    assert client_prof.status_code == 201
    client_data = client_prof.json()


async def test_create_client_profile_doc(ac: AsyncClient):
  for item in test_client_prof_doc:
    client_prof_doc = await ac.post('/clients/base/client_profile_doc', json=item)
    assert client_prof_doc.status_code == 201



# async def test_update_client_data(ac: AsyncClient):

# async def test_update_client_profile(ac: AsyncClient):

# async def test_update_client_doc(ac: AsyncClient):

# async def test_get_client_prof_doc(ac: AsyncClient):