from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .handlers import HotelHandler
from . import schemas
from core.database import get_db



router = APIRouter(
  prefix='/hotels',
  tags=['Hotels']
)


@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.HotelBaseResponse
)
async def create_hotel(
  body: schemas.CreateHotelRequest,
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  created_hotel = await hotel_handler._create_hotel(
    hotel_body=body
  )
  return created_hotel


@router.get(
  '/',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.HotelBaseResponse]
)
async def get_all_hotels(
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  hotels = await hotel_handler._get_all_hotels()
  return hotels



@router.get(
  '/{hotel_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.HotelBaseResponse
)
async def get_hotel_by_id(
  hotel_id: int,
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  hotel = await hotel_handler._get_one_hotel(hotel_id)
  return hotel



@router.get(
  '/with_rooms/',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.HotelWithRooms]
)
async def get_hotels_with_rooms(
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  hotels = await hotel_handler._get_all_hotels(flag=True)
  return hotels



@router.get(
  '/with_rooms/{hotel_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.HotelWithRooms
)
async def get_hotel_by_id_with_rooms(
  hotel_id: int,
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  hotel = await hotel_handler._get_one_hotel(hotel_id, flag=True)
  return hotel



@router.patch(
  '/{hotel_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.HotelBaseResponse
)
async def update_hotel(
  hotel_id: int,
  body: schemas.HotelUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  updated_hotel = await hotel_handler._update_hotel(
    hotel_id=hotel_id,
    hotel_body=body
  )
  return updated_hotel



@router.delete(
  '/{hotel_id}',
  status_code=status.HTTP_200_OK
)
async def delete_hotel(
  hotel_id: int,
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  deleted_hotel_id = await hotel_handler._delete_hotel_by_id(hotel_id)
  return deleted_hotel_id


@router.post(
  '/append_hotel_to_program',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ProgramHotelRoomResponse
)
async def append_hotel_to_program(
  body: schemas.AppendHotelAndRoomToProgram,
  session: AsyncSession = Depends(get_db)
):
  hotel_handler = HotelHandler(session)
  appended_hotel = await hotel_handler._append_hotel_and_rooms_to_program(
    body
  )
  return appended_hotel