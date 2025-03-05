from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest


from .test_data import test_staff, test_cost_items, test_expenses
from apps.staff import schemas





async def test_create_cost_items(ac: AsyncClient):
  for indx, item in enumerate(test_cost_items):
    cost = await ac.post('/staff/cost_items/', json=item)
    assert cost.status_code == 201
    cost_data = cost.json()
    cost_item = schemas.CostItemResponse(**cost_data)
    assert cost_item.id == indx + 1
    assert cost_item.title == item['title'].lower()


async def test_get_all_cost_items(ac: AsyncClient):
  costs = await ac.get('/staff/cost_items/')
  assert costs.status_code == 200
  cost_data = costs.json()
  assert len(cost_data) == len(test_cost_items)
  for item in cost_data:
    cost_item = schemas.CostItemResponse(**item)
    assert cost_item.title == test_cost_items[cost_item.id - 1]['title'].lower()



async def test_create_employees(ac: AsyncClient):
  for indx, item in enumerate(test_staff):
    empl_data = await ac.post('/staff/employee/', json=item)
    assert empl_data.status_code == 201
    empl_created_data = empl_data.json()
    empl = schemas.EmployeeResponse(**empl_created_data)
    assert empl.id == indx + 1


async def test_get_all_employees(ac: AsyncClient):
  empl_list = await ac.get('/staff/employee/')
  assert empl_list.status_code == 200
  empl_data = empl_list.json()
  assert len(empl_data) == len(test_staff)
  for indx, item in enumerate(empl_data):
    empl = schemas.EmployeeResponse(**item)
    assert empl.first_name == test_staff[empl.id - 1]['first_name']


async def test_get_one_item(ac: AsyncClient):
  data = await ac.get('/staff/employee/1')
  assert data.status_code == 200
  item_data = data.json()
  empl = schemas.EmployeeResponse(**item_data)
  assert empl.first_name == test_staff[0]['first_name']
  assert empl.position == test_staff[0]['position']
  costItem = await ac.get('/staff/cost_items/1')
  assert costItem.status_code == 200
  costItemDAta = costItem.json()
  cost_item = schemas.CostItemResponse(**costItemDAta)
  assert cost_item.title == test_cost_items[0]['title'].lower()




async def test_create_expenses(ac: AsyncClient):
  for item in test_expenses:
    exp = await ac.post('/staff/expenses/', json=item) 
    assert exp.status_code == 201
    expData = exp.json()
    expense_item = schemas.ExpenseResponse(**expData)
    assert expense_item.amount == item['amount']
    assert expense_item.category_id == item['category_id']


async def test_get_expenses(ac: AsyncClient):
  exp = await ac.get('/staff/expenses/')
  assert exp.status_code == 200
  expData = exp.json()
  assert len(expData) == len(test_expenses)




async def test_get_empl_expenses(ac: AsyncClient):
  emplExp = await ac.get('/staff/employee/employee_expenses/')
  assert emplExp.status_code == 200
  empExpData = emplExp.json()
  data = {} #{1: 2, 2: 1, 3: 2, 0: 2, 4: 1, 5: 2, 6: 1, 7: 1}
  for exp in test_expenses:
    emp = exp.get('employee_id', 0)
    if emp not in data:
      data[emp] = 1
    else:
      data[emp] = data[emp] + 1
  for item in empExpData:
    employer_expense = schemas.EmployeeWithExpensesResponse(**item)
    employer_exp_len = data[employer_expense.id]
    assert len(employer_expense.expenses) == employer_exp_len







