from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from .handler import ClientHandler
from . import schemas
from core.database import get_db


router = APIRouter(
  prefix='/clients',
  tags=['Clients']
)



@router.post(
  '/',
  status_code=status.HTTP_201_CREATED
)
async def create_client(
  body: schemas.CreateClient,
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  created_client = await client_handler._create_client(body)
  return created_client



@router.get(
  '/',
  status_code=status.HTTP_200_OK
)
async def get_clients(
  session: AsyncSession = Depends(get_db)
):
  client_handler = ClientHandler(session)
  clients = await client_handler._get_clients_list()
  return clients