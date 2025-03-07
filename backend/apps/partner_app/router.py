from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .handler import PartnerHandler, BankAccountHandler


from core.database import get_db
from . import schemas

router = APIRouter(
  prefix='/partners',
  tags=['Partners']
)


@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.PartnerBaseShow
)
async def create_partner(
  body: schemas.CreatePartnerBaseRequest,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  new_partner = await partner_handler._create_partner(body)
  return new_partner



@router.get(
  '/',
  status_code=status.HTTP_200_OK,
  response_model=list[schemas.PartnerBaseShow]
)
async def get_all_partners(
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  partners_list = await partner_handler._get_all_partners()
  return partners_list



@router.get(
  '/{partner_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.PartnerBaseShow
)
async def get_partner_item(
  partner_id: int,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  partner = await partner_handler._get_partner_by_id(partner_id)
  return partner



@router.patch(
  '/{partner_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.PartnerBaseShow
)
async def update_partner_item(
  partner_id: int,
  body: schemas.PartnerUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  updated_partner = await partner_handler._update_partner(
    partner_id=partner_id,
    body=body
  )
  return updated_partner



@router.delete(
  '/{partner_id}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def update_partner_item(
  partner_id: int,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  deleted_partner = await partner_handler._delete_partner_by_id(partner_id)
  return deleted_partner



@router.post(
  '/partner_with_bank/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.PartnerBankCreateResponse
)
async def create_partner_and_bank(
  body: schemas.CreatePartnerAndBank,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  created_partner = await partner_handler._create_partner_with_bank(body)
  return created_partner



@router.get(
  '/partner_with_bank/{partner_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.PartnerBankCreateResponse
)
async def get_partner_with_bank(
  partner_id: int,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  partner = await partner_handler._get_partner_by_id(
    partner_id=partner_id,
    flag=True
  )
  return partner