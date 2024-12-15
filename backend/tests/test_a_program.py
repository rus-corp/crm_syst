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



async def test_get_one_program(ac: AsyncClient):
  programs_list = await ac.get('/programs/')
  assert programs_list.status_code == 200
  programs_list_data = programs_list.json()
  program_slug = programs_list_data[0]['slug']
  programItem = await ac.get(f'/programs/{program_slug}')
  assert programItem.status_code == 200
  programItemData = programItem.json()
  program = schemas.ProgramBaseResponse(**programItemData)
  assert program.id == programs_list_data[0]['id']
  assert program.title == programs_list_data[0]['title']



async def test_update_program(ac: AsyncClient):
  updated_data = {'title': 'New Program Title'}
  programs_list = await ac.get('/programs/')
  assert programs_list.status_code == 200
  programs_list_data = programs_list.json()
  program_slug = programs_list_data[0]['slug']
  updatedProgramItem = await ac.patch(f'/programs/{program_slug}', json=updated_data)
  assert updatedProgramItem.status_code == 200
  updatedProgramJson = updatedProgramItem.json()
  programItem = await ac.get(f'/programs/{program_slug}')
  assert programItem.status_code == 200
  programDataJson = programItem.json()
  program = schemas.ProgramBaseResponse(**programDataJson)
  assert program.id == updatedProgramJson['id']
  assert program.title == updated_data['title']


