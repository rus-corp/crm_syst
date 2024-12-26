from httpx import AsyncClient

from apps.program_app import schemas
from apps.hotels_app.hotels import schemas as hotel_schema
from apps.hotels_app.hotel_rooms import schemas as room_schema
from apps.staff import schemas as emp_schemas




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


async def test_update_cost(ac: AsyncClient):
  update_data = {'title': 'BTA'}
  cost_db = await ac.get('/staff/cost_items/1')
  assert cost_db.status_code == 200
  costData = cost_db.json()
  cost_item = emp_schemas.CostItemResponse(**costData)
  updatedCost = await ac.patch('/staff/cost_items/1', json=update_data)
  assert updatedCost.status_code == 200
  updatedCostData = updatedCost.json()
  updated_cost = emp_schemas.CostItemResponse(**updatedCostData)
  assert updated_cost.id == cost_item.id
  assert updated_cost.title.lower() != cost_item.title




async def test_update_one_expense(ac: AsyncClient):
  updated_data = {'employee_id': 3}
  expeDb = await ac.get('/staff/expenses/1')
  assert expeDb.status_code == 200
  expData = expeDb.json()
  exp_before = emp_schemas.ExpenseFullResponse(**expData)
  update_req = await ac.patch('/staff/expenses/1', json=updated_data)
  assert update_req.status_code == 200
  updated_res = await ac.get('/staff/expenses/1')
  assert updated_res.status_code == 200
  updatedData = updated_res.json()
  expense_after = emp_schemas.ExpenseFullResponse(**updatedData)
  assert expense_after.id == exp_before.id
  assert expense_after.amount == exp_before.amount
  assert expense_after.category_id == exp_before.category_id
  assert expense_after.employee_id != exp_before.employee_id






# async def test_delete_hotel_from_programm(ac: AsyncClient):...

# async def test_delete_hotel(ac: AsyncClient):...

# async def test_delete_hotel_room(ac: AsyncClient):...