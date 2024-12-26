from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest

from .test_data import test_program_expenses, program_test_data
from apps.base.base_schemas import BaseMessageResponseModel

async def test_append_exp_to_prog(ac: AsyncClient):
  for item in test_program_expenses:
    programExpense = await ac.post('/programs/program_expenses', json=item)
    assert programExpense.status_code == 201
    programExpenseDAta = programExpense.json()
    # print(programExpenseDAta)
    programTitle = programExpenseDAta.split('Program')
    assert programTitle[1].strip() == program_test_data[item['program_id'] - 1]['title']



# async def test_append_client_to_program(ac: AsyncClient):
#   programClient = await ac.post('/programs/append_client/')



# async def test_append_hotel_and_room_to_program(ac: AsyncClient):...










# async def create_client_family(ac: AsyncClient)

# async def get_client_family(ac: AsyncClient):

# async def test_get_program_clients(ac: AsyncClient):...


# async def test_append_client_to_program(ac: AsyncClient):...

# async def test_delete_client_to_program(ac: AsyncClient):...

# async def test_append_hotel_to_program(ac: AsyncClient):...