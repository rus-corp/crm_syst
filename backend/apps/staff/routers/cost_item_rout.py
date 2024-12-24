from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db


from ..handlers.cost_item_handler import CostItemHandler
from .. import schemas


router = APIRouter(
  prefix='/cost_items',
  tags=['Cost Items']
)


@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.CostItemResponse
)
async def create_cost_item(
  body: schemas.CostItemBase,
  session: AsyncSession = Depends(get_db)
):
  cost_handler = CostItemHandler(session)
  cost_item = await cost_handler._create_cost_item(body)
  return cost_item



@router.get(
  '/',
  status_code=status.HTTP_200_OK,
  response_model=List[schemas.CostItemResponse]
)
async def get_all_cost_items(
  session: AsyncSession = Depends(get_db)
):
  cost_handler = CostItemHandler(session)
  cost_items = await cost_handler._get_all_cost_items()
  return cost_items



@router.get(
  '/{item_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.CostItemResponse
)
async def get_cost_item_by_id(
  item_id: int,
  session: AsyncSession = Depends(get_db)
):
  cost_handler = CostItemHandler(session)
  cost_item = await cost_handler._get_cost_item(item_id)
  return cost_item


@router.patch(
  '/{item_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.CostItemResponse
)
async def update_cost_item_by_id(
  item_id: int,
  body: schemas.CostItemBase,
  session: AsyncSession = Depends(get_db)
):
  cost_handler = CostItemHandler(session)
  cost_item = await cost_handler._update_cost_item(
    cost_item_id=item_id,
    cost_body=body
  )
  return cost_item


@router.delete(
  '/{item_id}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def delete_cost_item_by_id(
  item_id: int,
  session: AsyncSession = Depends(get_db)
):
  cost_handler = CostItemHandler(session)
  deleted_item = await cost_handler._delete_cost_item(item_id)
  return deleted_item