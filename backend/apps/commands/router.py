from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from apps.client_app.dals import ClientDAL
from apps.hotels_app.hotels.dals import HotelDAL
from apps.hotels_app.hotel_rooms.dals import HotelRoomsDAL
from apps.utils.slug import create_slug

from .data import clients, hotel_rooms, hotels




router = APIRouter(
  prefix='/commands',
  tags=['Coma']
)


@router.get('/')
async def create_data(session: AsyncSession = Depends(get_db)):
  client_dal = ClientDAL(session)
  for client in clients:
    slug = create_slug(client['last_name'] + client['name'])
    client['slug'] = slug
    new_client = await client_dal.create_client(**client)
  return {'status': 'created'}



@router.get('/hot')
async def create_h(session: AsyncSession = Depends(get_db)):
  hot_dal = HotelDAL(session)
  for hot in hotels:
    new_hot = await hot_dal.create_hotel(**hot)
  return {'status': 'created'}

@router.get('/ro')
async def create_ro(session: AsyncSession = Depends(get_db)):
  room_dal = HotelRoomsDAL(session)
  for r in hotel_rooms:
    new_r = await room_dal.create_room(**r)
  return {'status': 'created'}