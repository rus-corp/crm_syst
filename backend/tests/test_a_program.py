from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest

from .test_data import program_test_data
from apps.program_app import schemas



async def test_create_program(ac: AsyncClient):
  for item in program_test_data:
    prog = await ac.post('/programs/', json=item)
    assert prog.status_code == 201
  program_db = await ac.get('/programs/')
  assert program_db.status_code == 200
  program_data = program_db.json()
  assert len(program_data) == len(program_test_data)
  for prog in program_data:
    program = schemas.ProgramBaseResponse(**prog)
    assert program.id == prog['id']
  for i in program_data:
    id = i['id']
    assert i['title'] == program_test_data[id - 1]['title']



# async def test_get_one_program(ac: AsyncClient):
  

# async def test_update_program(ac: AsyncClient):...


