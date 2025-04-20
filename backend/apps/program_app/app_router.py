from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status

from .routers.program_router import router as program_router
from .routers.pro_price_router import router as program_price_router



router = APIRouter(
  prefix='/program',
  tags=['Program']
)

router.include_router(program_router)
router.include_router(program_price_router)