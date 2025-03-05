from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .handler import PartnerHandler, BankAccountHandler


from core.database import get_db
from . import schemas

router = APIRouter(
  prefix='/partners',
  tags=['Partners']
)


# @router.post(
#   '/',
#   status_code=status.HTTP_200_OK
# )
# async def create_partner(
#   body: schemas.CreatePartnerBaseRequest,
#   session: AsyncSession = Depends(get_db)
# ):
#   partner_handler = PartnerHandler(session)
#   new_partner = await partner_handler._create_partner(body)
#   return new_partner

# @router.get
# @router.get
# @router.patch
# @router.delete