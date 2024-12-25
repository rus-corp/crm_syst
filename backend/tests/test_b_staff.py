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
    assert cost_item.title == item['title']


async def test_get_all_cost_items(ac: AsyncClient):
  costs = await ac.get('/staff/cost_items/')
  assert costs.status_code == 200
  cost_data = costs.json()
  assert len(cost_data) == len(test_cost_items)
  for item in cost_data:
    cost_item = schemas.CostItemResponse(**item)
    assert cost_item.title == test_cost_items[cost_item.id - 1]['title']



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
  assert cost_item.title == test_cost_items[0]['title']



async def test_update_empl(ac: AsyncClient):
  update_empl_data = {'position': 'Астроном'}
  empl_db = await ac.get('/staff/employee/1')
  assert empl_db.status_code == 200
  emplDbData = empl_db.json()
  empl_before = schemas.EmployeeResponse(**emplDbData)
  update_empl = await ac.patch('/staff/employee/1', json=update_empl_data)
  assert update_empl.status_code == 200
  updateEmplDAta = update_empl.json()
  update_empl = schemas.EmployeeResponse(**updateEmplDAta)
  assert update_empl.id == empl_before.id
  assert update_empl.first_name == empl_before.first_name
  assert update_empl.position != empl_before.position
  bad_data = {'position': 'BANK'}
  bad_req = await ac.patch('/staff/employee/1', json=bad_data)
  assert bad_req != 200




async def test_update_cost(ac: AsyncClient):
  update_data = {'title': 'BTA'}
  cost_db = await ac.get('/staff/cost_items/1')
  assert cost_db.status_code == 200
  costData = cost_db.json()
  cost_item = schemas.CostItemResponse(**costData)
  updatedCost = await ac.patch('/staff/cost_items/1', json=update_data)
  assert updatedCost.status_code == 200
  updatedCostData = updatedCost.json()
  updated_cost = schemas.CostItemResponse(**updatedCostData)
  assert updated_cost.id == cost_item.id
  assert updated_cost.title != cost_item.title




async def test_create_expenses(ac: AsyncClient):
  for item in test_expenses:
    exp = await ac.post('/staff/expenses/', json=item) 
    assert exp.status_code == 201
    expData = exp.json()
    expense_item = schemas.ExpenseBaseResponse(**expData)
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


async def test_update_one_expense(ac: AsyncClient):
  updated_data = {'employee_id': 3}
  expeDb = await ac.get('/staff/expenses/1')
  assert expeDb.status_code == 200
  expData = expeDb.json()
  exp_before = schemas.ExpenseFullResponse(**expData)
  update_req = await ac.patch('/staff/expenses/1', json=updated_data)
  assert update_req.status_code == 200
  updated_res = await ac.get('/staff/expenses/1')
  assert updated_res.status_code == 200
  updatedData = updated_res.json()
  expense_after = schemas.ExpenseFullResponse(**updatedData)
  assert expense_after.id == exp_before.id
  assert expense_after.amount == exp_before.amount
  assert expense_after.category_id == exp_before.category_id
  assert expense_after.employee_id != exp_before.employee_id




# async def test_append_exp_to_prog(ac: AsyncClient)