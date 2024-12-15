from httpx import AsyncClient

from .test_data import test_hotels, test_hotel_rooms
from apps.hotels_app.hotels import schemas
from apps.hotels_app.hotel_rooms import schemas as room_schema


async def test_create_hotel(ac: AsyncClient):
  for item in test_hotels:
    hotel = await ac.post('/hotels/', json=item)
    assert hotel.status_code == 201
    hotel_data = hotel.json()
    hotelItem = schemas.HotelBaseResponse(**hotel_data)
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
  hotelItem = schemas.HotelBaseResponse(**hotel_data)
  assert hotelItem.title == test_hotels[0]['title']
  assert hotelItem.city == test_hotels[0]['city']


async def test_update_hotel(ac: AsyncClient):
  updated_data = {'title': 'New Item Title'}
  hotel = await ac.patch('/hotels/1', json=updated_data)
  assert hotel.status_code == 200
  updated_hotel = await ac.get('/hotels/1')
  assert updated_hotel.status_code == 200
  hotel_data = updated_hotel.json()
  hotelItem = schemas.HotelBaseResponse(**hotel_data)
  assert hotelItem.title == updated_data['title']


# async def test_create_hotel_rooom(ac: AsyncClient):...


# async def test_get_hotel_rooms(ac: AsyncClient):...


# async def test_update_hotel_room(ac: AsyncClient):...


# async def test_append_hotel_to_program(ac: AsyncClient):...


# async def test_delete_hotel_from_programm(ac: AsyncClient):...

# async def test_delete_hotel(ac: AsyncClient):...

# async def test_delete_hotel_room(ac: AsyncClient):...