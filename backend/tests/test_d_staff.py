from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest


from .test_data import test_staff, test_expenses
from apps.staff import schemas



async def test_create_employees(ac: AsyncClient):
  for indx, item in enumerate(test_staff):
    empl_data = await ac.post('/staff/', json=item)
    assert empl_data.status_code == 201
    empl_created_data = empl_data.json()
    empl = schemas.EmployeeResponse(**empl_created_data)
    assert empl.id == indx + 1


async def test_get_all_items(ac: AsyncClient):
  empl_list = await ac.get('/staff/')
  assert empl_list.status_code == 200
  empl_data = empl_list.json()
  assert len(empl_data) == len(test_staff)
  for indx, item in enumerate(empl_data):
    empl = schemas.EmployeeResponse(**item)
    assert empl.first_name == test_staff[empl.id - 1]['first_name']


async def test_get_one_item(ac: AsyncClient):
  data = await ac.get('/staff/1')
  assert data.status_code == 200
  item_data = data.json()
  empl = schemas.EmployeeResponse(**item_data)
  assert empl.first_name == test_staff[0]['first_name']
  assert empl.position == test_staff[0]['position']


# async def test_update_empl(ac: AsyncClient):


# async def test_create_expenses(ac: AsyncClient)

# async def test_get_empl_expenses(ac: AsyncClient)


# async def test_append_exp_to_prog(ac: AsyncClient)