from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .handler import PartnerHandler, BankAccountHandler, PartnerServiceHandler


from core.database import get_db
from core.models.utils import PartnerCategory
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
  response_model=list[schemas.CreatePartnerAndServiceResponse]
)
async def get_all_partners(
  category: PartnerCategory = None,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  partners_list = await partner_handler._get_all_partners(category)
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
  '/partner_with_service/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.CreatePartnerAndServiceResponse
)
async def create_partner_and_service(
  body: schemas.CreatePartnerAndServiceRequest,
  session: AsyncSession = Depends(get_db)
):
  partner_handler = PartnerHandler(session)
  created_partner = await partner_handler._create_partner_with_service(body)
  return created_partner



@router.get(
  '/partner_with_service_and_bank/{partner_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.PartnerBankServiceResponse
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



@router.post(
  '/partner_service/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.PartnerServiceBaseResponse
)
async def create_partner_service(
  body: schemas.PartnerServiceCreateRequest,
  session: AsyncSession = Depends(get_db)
):
  service_handler = PartnerServiceHandler(session)
  created_service = await service_handler._create_partner_service(body)
  return created_service



@router.get(
  '/partner_service/{service_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.PartnerServiceBaseResponse
)
async def get_service_item(
  service_id: int,
  session: AsyncSession = Depends(get_db)
):
  service_handler = PartnerServiceHandler(session)
  service_item = await service_handler._get_service_item(service_id)
  return service_item



@router.patch(
  '/partner_service/{service_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.PartnerServiceBaseResponse
)
async def update_partner_service(
  service_id: int,
  body: schemas.PartnerServiceUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  service_handler = PartnerServiceHandler(session)
  updated_service = await service_handler._update_partner_service(
    service_id=service_id,
    body=body
  )
  return updated_service



@router.delete(
  '/partner_service/{service_id}',
  status_code=status.HTTP_204_NO_CONTENT,
  # response_model=
)
async def delete_partner_service(
  service_id: int,
  session: AsyncSession = Depends(get_db)
):
  service_handler = PartnerServiceHandler(session)
  deleted_service = await service_handler._delete_partner_service(service_id)
  return deleted_service



@router.post(
  '/partner_bank/',
  status_code=status.HTTP_201_CREATED,
  # response_model=
)
async def create_partner_bank(
  body: schemas.BankAccountPartnerCreateRequest,
  session: AsyncSession = Depends(get_db)
):
  bank_handler = BankAccountHandler(session)
  created_account = await bank_handler._create_bank_item(body)
  return created_account


@router.get(
  '/partner_bank/{bank_account}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.BankAccountShowBase
)
async def get_bank_account_by_id(
  bank_account: int,
  session: AsyncSession = Depends(get_db)
):
  bank_handler = BankAccountHandler(session)
  bank_account_data = await bank_handler._get_bank_account_by_id(bank_account)
  return bank_account_data



@router.patch(
  '/partner_bank/{bank_account}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.BankAccountShowBase
)
async def update_bank_account_by_id(
  bank_account: int,
  body: schemas.BankAccountUpdateRequest,
  session: AsyncSession = Depends(get_db)
):
  bank_handler = BankAccountHandler(session)
  bank_account_data = await bank_handler._update_bank_account(
    account_id=bank_account,
    values=body
  )
  return bank_account_data


@router.delete(
  '/partner_bank/{bank_account}',
  status_code=status.HTTP_204_NO_CONTENT
)
async def delete_bank_account_by_id(
  bank_account: int,
  session: AsyncSession = Depends(get_db)
):
  bank_handler = BankAccountHandler(session)
  deleted_account = await bank_handler._delete_bank_account(
    account_id=bank_account,
  )
  return deleted_account

