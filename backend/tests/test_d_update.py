from httpx import AsyncClient

from apps.program_app import schemas
from apps.hotels_app.hotels import schemas as hotel_schema
from apps.hotels_app.hotel_rooms import schemas as room_schema
from apps.staff import schemas as emp_schemas
from apps.partner_app import schemas as partner_schemas



async def test_update_program(ac: AsyncClient):
  updated_data = {'title': 'New Program Title'}
  programs_list = await ac.get('/program/base/')
  assert programs_list.status_code == 200
  programs_list_data = programs_list.json()
  program_slug = programs_list_data[0]['slug']
  updatedProgramItem = await ac.patch(f'/program/base/{program_slug}', json=updated_data)
  assert updatedProgramItem.status_code == 200
  updatedProgramJson = updatedProgramItem.json()
  programItem = await ac.get(f'/program/base/{program_slug}')
  assert programItem.status_code == 200
  programDataJson = programItem.json()
  program = schemas.ProgramBaseResponse(**programDataJson)
  assert program.id == updatedProgramJson['id']
  assert program.title == updated_data['title']



async def test_update_hotel(ac: AsyncClient):
  updated_data = {'title': 'New Item Title'}
  hotel = await ac.patch('/hotels/1', json=updated_data)
  assert hotel.status_code == 200
  updated_hotel = await ac.get('/hotels/1')
  assert updated_hotel.status_code == 200
  hotel_data = updated_hotel.json()
  hotelItem = hotel_schema.HotelBaseResponse(**hotel_data)
  assert hotelItem.title == updated_data['title']



async def test_update_room(ac: AsyncClient):
  room_data = await ac.get('/rooms/1')
  assert room_data.status_code == 200
  room_db = room_data.json()
  room = room_schema.HotelRoomBaseResponse(**room_db)
  updated_data = {'room_price': 9999}
  updated_room_req = await ac.patch('/rooms/1', json=updated_data)
  assert updated_room_req.status_code == 200
  updated_room_data = updated_room_req.json()
  updated_room = room_schema.HotelRoomBaseResponse(**updated_room_data)
  assert updated_room.id == room.id
  assert updated_room.room_type == room.room_type
  assert updated_room.room_volume == room.room_volume
  assert updated_room.room_price == updated_data['room_price']



async def test_update_empl(ac: AsyncClient):
  update_empl_data = {'position': 'Астроном'}
  empl_db = await ac.get('/staff/employee/1')
  assert empl_db.status_code == 200
  emplDbData = empl_db.json()
  empl_before = emp_schemas.EmployeeResponse(**emplDbData)
  update_empl = await ac.patch('/staff/employee/1', json=update_empl_data)
  assert update_empl.status_code == 200
  updateEmplDAta = update_empl.json()
  update_empl = emp_schemas.EmployeeResponse(**updateEmplDAta)
  assert update_empl.id == empl_before.id
  assert update_empl.first_name == empl_before.first_name
  assert update_empl.position != empl_before.position
  bad_data = {'position': 'BANK'}
  bad_req = await ac.patch('/staff/employee/1', json=bad_data)
  assert bad_req != 200



async def test_update_partner(ac: AsyncClient):
  new_data = {"category": 'Экскурсии'}
  partnerBefore = await ac.get('/partners/1')
  assert partnerBefore.status_code == 200
  partnerBeforeJson = partnerBefore.json()
  partner_before = partner_schemas.PartnerBaseShow(**partnerBeforeJson)
  updatePartner = await ac.patch('/partners/1', json=new_data)
  assert updatePartner.status_code == 200
  updatePartnerJson = updatePartner.json()
  updated_partner = partner_schemas.PartnerBaseShow(**updatePartnerJson)
  assert updated_partner.title == partner_before.title
  assert updated_partner.id == partner_before.id
  assert updated_partner.category != partner_before.category



async def test_update_partner_service(ac: AsyncClient):
  new_data = {'price': 99999}
  service_before = await ac.get('/partners/partner_service/2')
  assert service_before.status_code == 200
  serviceBeforeJson = service_before.json()
  service_before_data = partner_schemas.PartnerServiceBaseResponse(**serviceBeforeJson)
  updated_service_req = await ac.patch('/partners/partner_service/2', json=new_data)
  assert updated_service_req.status_code == 200
  updatedServiceJson = updated_service_req.json()
  updated_service_data = partner_schemas.PartnerServiceBaseResponse(**updatedServiceJson)
  assert updated_service_data.id == service_before_data.id
  assert updated_service_data.service_name == service_before_data.service_name
  assert updated_service_data.price != service_before_data.price


async def test_update_bank_account(ac: AsyncClient):
  new_data = {'bic': '99999999'}
  bank_before = await ac.get('/partners/partner_bank/2')
  assert bank_before.status_code == 200
  bank_beforeJson = bank_before.json()
  bank_before_data = partner_schemas.BankAccountShowBase(**bank_beforeJson)
  updated_bank = await ac.patch('/partners/partner_bank/2', json=new_data)
  assert updated_bank.status_code == 200
  updated_bankJson = updated_bank.json()
  updated_bank_data = partner_schemas.BankAccountShowBase(**updated_bankJson)
  assert updated_bank_data.id == bank_before_data.id
  assert updated_bank_data.account_number == bank_before_data.account_number
  assert updated_bank_data.bic != bank_before_data.bic
  assert updated_bank_data.bic == new_data['bic']


# async def test_delete_hotel_from_programm(ac: AsyncClient):...

# async def test_delete_hotel(ac: AsyncClient):...

# async def test_delete_hotel_room(ac: AsyncClient):...