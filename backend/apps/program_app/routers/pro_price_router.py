from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status
from apps.hotels_app.hotels.schemas import HotelWithRooms



from core.database import get_db
from .. import schemas
from ..handlers.program_handler import ProgramHandler
from apps.base.base_schemas import BaseMessageResponseModel




router = APIRouter(
  prefix='/price',
  tags=['Program Prices']
)


@router.post(
  '/{program_id}',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.ProgramPricesBaseResponse
)
async def calculate_program_prices(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_prices = await program_handler._calculate_program_prices(program_id)
  return program_prices


@router.get(
  '/{program_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.ProgramPricesResponse
)
async def get_program_prices(
  program_id: int,
  session: AsyncSession = Depends(get_db)
):
  program_handler = ProgramHandler(session)
  program_prices = await program_handler._get_program_prices(program_id)
  return program_prices