from apps.base.base_dal import BaseDAL
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from core.models.staff_models import Employee



class EmployeeDAL(BaseDAL):
  model = Employee
  
  async def get_or_create_employee(self, values):
    result = await self.base_get_or_create(
      model=self.model,
      values=values
    )
    return result
  
  
  async def create_employee(self, values: dict):
    result = await self.base_create_item(
      model=self.model,
      values=values
    )
    return result
  
  
  async def get_all_employees(self):
    query = select(self.model).order_by(self.model.id)
    result = await self.db_session.execute(query)
    return result.scalars().unique().all()
  
  
  async def get_one_employee(self, employee_id: int):
    result = await self.base_get_one_item(
      model=self.model,
      item_id=employee_id
    )
    return result
  
  
  async def update_employee(self, employee_id: int, values):
    result = await self.base_update_item(
      model=self.model,
      item_id=employee_id,
      values=values
    )
    return result
  
  
  async def delete_employee(self, employee_id: int):
    result = await self.base_delete_item(
      model=self.model,
      item_id=employee_id
    )
    return result
  
  
  async def get_employee_by_id_with_expenses(self, employee_id: int):
    query = (select(Employee)
             .where(Employee.id == employee_id)
             .options(joinedload(Employee.expenses)))
    result = await self.db_session.execute(query)
    return result.scalar()
  
  
  async def get_all_employees_with_expenses(self, limit: int = None):
    if limit:
      query = (select(Employee)
               .options(joinedload(Employee.expenses))
               .limit(limit))
    else:
      query = (select(Employee)
              .options(selectinload(Employee.expenses)))
    result = await self.db_session.execute(query)
    return result.scalars().unique().all()