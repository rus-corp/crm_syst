from typing import List
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
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.HotelRoomBaseResponse
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
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.HotelRoomBaseResponse]
)
async def get_all_rooms(
  session: AsyncSession = Depends(get_db)
):
  room_handler = HotelRoomsHandler(session)
  rooms = await room_handler._get_all_rooms()
  return rooms


@router.get(
  '/{room_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.HotelRoomBaseResponse
)
async def get_room_by_id(
  room_id: int,
  session: AsyncSession = Depends(get_db)
):
  room_handler = HotelRoomsHandler(session)
  room = await room_handler._get_room_item(room_id)
  return room


@router.patch(
  '/{room_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.HotelRoomBaseResponse
)
async def update_room_by_id(
  room_id: int,
  body: schemas.HotelRoomUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  room_handler = HotelRoomsHandler(session)
  room = await room_handler._update_room(
    room_id=room_id,
    room_body=body
  )
  return room



@router.delete(
  '/{room_id}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def delete_hotel_room_by_id(
  room_id: int,
  session: AsyncSession = Depends(get_db)
):
  room_handler = HotelRoomsHandler(session)
  room = await room_handler._delete_room_by_id(room_id)
  return room



@router.post(
  '/room_list/',
  status_code=status.HTTP_201_CREATED,
  response_model=list[schemas.HotelRoomBaseResponse]
)
async def create_rooms_list(
  list_body: list[schemas.HoteRoomCreateRequset],
  session: AsyncSession = Depends(get_db)
):
  room_handler = HotelRoomsHandler(session)
  created_room = await room_handler._create_many_hotel_rooms(list_body)
  return created_room