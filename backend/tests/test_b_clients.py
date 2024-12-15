from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest



from .test_data import test_clients_data, test_client_details, test_client_documents




async def test_create_clients(ac: AsyncClient):
  for item in test_clients_data:
    client = await ac.post('/clients/', json=item)
    assert client.status_code == 201
  
  client_db = await ac.get('/clients/')
  assert client_db.status_code == 200
  client_db_data = client_db.json()
  assert len(client_db_data) == len(test_clients_data)
  for cli in client_db_data:
    id = cli['id']
    assert cli['last_name'] == test_clients_data[id - 1]['last_name']
    assert cli['name'] == test_clients_data[id - 1]['name']




async def test_create_client_profile(ac: AsyncClient):
  for item in test_client_details:
    client_profile = await ac.post('')

# async def test_create_client_doc(ac: AsyncClient):...


# async def test_get_one_item(ac: AsyncClient): ...

# async def test_update_client_data(ac: AsyncClient):

# async def test_update_client_profile(ac: AsyncClient):

# async def test_update_client_doc(ac: AsyncClient):

# async def test_get_client_prof_doc(ac: AsyncClient):


# async def create_client_family(ac: AsyncClient)

# async def get_client_family(ac: AsyncClient):

# async def test_get_program_clients(ac: AsyncClient):...


# async def test_append_client_to_program(ac: AsyncClient):...

# async def test_delete_client_to_program(ac: AsyncClient):...