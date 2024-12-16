from fastapi import APIRouter



from .client.routers import router as data_router
from .client_profile.router import router as profile_router
from .client_doc.routers import router as doc_router


router = APIRouter(
  prefix='/clients',
  tags=['Clients App']
)



router.include_router(data_router)
router.include_router(profile_router)
router.include_router(doc_router)