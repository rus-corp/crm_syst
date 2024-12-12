from apps.base.base_dal import BaseDAL
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload, joinedload




from core.models.staff_models import Employee, Expenses




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
    result = await self.base_get_all_items(
      model=self.model
    )
    return result
  
  
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
  
  
  async def get_all_employees_with_expenses(self):
    query = (select(Employee)
             .options(selectinload(Employee.expenses)))
    result = await self.db_session.execute(query)
    return result.scalars().all()





class ExpensesDAL(BaseDAL):
  model = Expenses
  
  async def get_or_create_expenses(self, values: dict):
    result = await self.base_get_or_create(
      model=self.model,
      values=values
    )
    return result
  
  
  async def get_all_expenses(self):
    return await self.base_get_all_items(self.model)
  
  
  async def get_one_expense(self, exp_id: int):
    return await self.base_get_one_item(
      model=self.model,
      item_id=exp_id
    )
  
  
  async def update_expense(self, expense_id: int, values: dict):
    return await self.base_update_item(
      model=self.model,
      item_id=expense_id,
      values=values
    )
  
  
  async def delete_expense(self, expense_id: int):
    return await self.base_delete_item(
      model=self.model,
      item_id=expense_id
    )
  
  
  async def get_expenses_with_employee(self, expense_id: int):
    query = select(Expenses).where(Expenses.id == expense_id).options(joinedload(Expenses.employee))
    return await self.db_session.scalar(query)
  
  
  async def create_many_items(self, values: list[dict]):
    query = insert(self.model).values(values).returning(self.model)
    result = await self.db_session.execute(query)
    await self.db_session.commit()
    return result.scalars().all()