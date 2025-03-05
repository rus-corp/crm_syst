from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.database import get_db
from . import schemas
from .handler import ClientDocumentHandler
from apps.base.base_schemas import BaseMessageResponseModel



router = APIRouter(
  prefix='/doc',
  tags=['Docs']
)


@router.post(
  '/',
  status_code=status.HTTP_201_CREATED,
  response_model=schemas.DocumentResponse,
  responses={
    404: {'model': BaseMessageResponseModel}
  }
)
async def create_client_doc(
  body: schemas.CreateDocumentRequest,
  session: AsyncSession = Depends(get_db)
):
  doc_handler = ClientDocumentHandler(session)
  client_doc = await doc_handler._create_client_doc(body)
  return client_doc



@router.get(
  '/{client_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.DocumentResponse
)
async def get_client_doc(
  client_id: int,
  session: AsyncSession = Depends(get_db)
):
  doc_handler = ClientDocumentHandler(session)
  client_doc = await doc_handler._get_client_doc(client_id)
  return client_doc



@router.patch(
  '/{client_id}',
  status_code=status.HTTP_200_OK,
  response_model=schemas.DocumentResponse
)
async def update_client_doc(
  client_id: int,
  body: schemas.UpdateDocumentRequest,
  session: AsyncSession = Depends(get_db)
):
  doc_handler = ClientDocumentHandler(session)
  client_doc = await doc_handler._update_client_doc(
    client_id=client_id,
    values=body
  )
  return client_doc