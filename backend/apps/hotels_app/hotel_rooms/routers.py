from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas
from core.database import get_db
from .handlers import HotelRoomsHandler


router = APIRouter(
  prefix='/rooms',
  tags=['Rooms']
)


@router.post(
  '/',
  status_code=status.HTTP_201_CREATED
)
async def create_romm(
  body: schemas.HoteRoomCreateRequset,
  session: AsyncSession = Depends(get_db)
):
  room_handler = HotelRoomsHandler(session)
  created_room = await room_handler._create_hotel_room(body)
  return created_room



@router.get(
  '/',
  status_code=status.HTTP_200_OK
)
async def get_all_rooms(
  session: AsyncSession = Depends(get_db)
):
  room_handler = HotelRoomsHandler(session)
  rooms = await room_handler._get_all_rooms()
  return rooms