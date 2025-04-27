from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status



from core.database import get_db
from .handlers import ProgramRoomsHandler



router = APIRouter(
  prefix='/program_rooms',
  tags=['Program Rooms']
)


@router.get(
  '/{program_room_id}',
  status_code=status.HTTP_200_OK
)
async def get_program_room_client(
  program_room_id: int,
  session = Depends(get_db)
):
  program_room_handler = ProgramRoomsHandler(session)
  program_room_clients = await program_room_handler._get_program_room_clients(program_room_id)
  return program_room_clients