from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest



from .test_data import test_clients_data, test_client_details, test_client_documents
from apps.client_app.client_profile.schemas import ProfileResponse
from apps.client_app.client_doc.schemas import DocumentResponse
from apps.client_app.schemas import BaseShowClient


async def test_create_clients(ac: AsyncClient):
  for item in test_clients_data:
    client = await ac.post('/clients/base/', json=item)
    assert client.status_code == 201
  
  client_db = await ac.get('/clients/base/')
  assert client_db.status_code == 200
  client_db_data = client_db.json()
  assert len(client_db_data) == len(test_clients_data)
  for cli in client_db_data:
    id = cli['id']
    assert cli['last_name'] == test_clients_data[id - 1]['last_name']
    assert cli['name'] == test_clients_data[id - 1]['name']




async def test_create_client_profile(ac: AsyncClient):
  for item in test_client_details[:-1]:
    client_profile = await ac.post('/clients/profile/', json=item)
    assert client_profile.status_code == 201
    profile_data = client_profile.json()
    profile = ProfileResponse(**profile_data)
    assert profile.shirt_size == item['shirt_size']
    assert profile.city == item['city']
  bad_req = await ac.post('/clients/profile/', json=test_client_details[-1])
  assert bad_req.status_code == 404


async def test_create_client_doc(ac: AsyncClient):
  for item in test_client_documents[:-1]:
    doc = await ac.post('/clients/doc/', json=item)
    assert doc.status_code == 201
    doc_data = doc.json()
    docum = DocumentResponse(**doc_data)
    assert docum.doc_type == item['doc_type']
    assert docum.series == item['series']
    assert docum.number == item['number']
  bad_req = await ac.post('/clients/doc/', json=test_client_documents[-1])
  assert bad_req.status_code == 404



async def test_list_items(ac: AsyncClient):
  client_req = await ac.get('/clients/base/')
  assert client_req.status_code == 200
  client_data = client_req.json()
  for item in client_data:
    id = item['id']
    client = BaseShowClient(**item)
    client.name == test_clients_data[id - 1]['name']
    client.last_name == test_clients_data[id - 1]['last_name']




# async def test_get_client_prof_doc(ac: AsyncClient):




# async def test_update_client_data(ac: AsyncClient):

# async def test_update_client_profile(ac: AsyncClient):

# async def test_update_client_doc(ac: AsyncClient):



# async def create_client_family(ac: AsyncClient)

# async def get_client_family(ac: AsyncClient):

# async def test_get_program_clients(ac: AsyncClient):...


# async def test_append_client_to_program(ac: AsyncClient):...

# async def test_delete_client_to_program(ac: AsyncClient):...