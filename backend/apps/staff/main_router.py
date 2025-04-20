from fastapi import APIRouter

# from .routers.cost_item_rout import router as cost_rout
from .routers.employee_rout import router as employee_rout
from .routers.expenses_rout import router as expense_rout



router = APIRouter(
  prefix='/staff',
  tags=['Staff']
)


# router.include_router(cost_rout)
router.include_router(employee_rout)
router.include_router(expense_rout)











