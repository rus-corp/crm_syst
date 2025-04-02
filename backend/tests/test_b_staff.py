from httpx import AsyncClient
from fastapi.exceptions import HTTPException
import pytest


from .test_data import (
  test_staff,
  test_expenses, test_partners_data,
  test_static_and_employee_expense_data,
  test_partner_bank_data,
  test_partner_service_data,
  test_partner_and_services_data
)
from apps.staff import schemas
from apps.partner_app import schemas as partner_schemas




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



async def test_create_expense_and_employee_data(ac: AsyncClient):
  print(test_static_and_employee_expense_data)
  req_data = await ac.post('/staff/expenses/create_static_and_employee_expense/', json=test_static_and_employee_expense_data)
  assert req_data.status_code == 201


async def test_get_one_item(ac: AsyncClient):
  data = await ac.get('/staff/employee/1')
  assert data.status_code == 200
  item_data = data.json()
  empl = schemas.EmployeeResponse(**item_data)
  assert empl.first_name == test_staff[0]['first_name']
  assert empl.position == test_staff[0]['position']



async def test_create_partner(ac: AsyncClient):
  for indx, item in enumerate(test_partners_data):
    partnerCreated = await ac.post('/partners/', json=item)
    assert partnerCreated.status_code == 201
    partnerData = partnerCreated.json()
    partner = partner_schemas.PartnerBaseShow(**partnerData)
    assert partner.id == indx + 1
    assert partner.title == item['title']
    assert partner.law_title == item['law_title']
  partnersList = await ac.get('/partners/')
  assert partnersList.status_code == 200
  partnersListData = partnersList.json()
  assert len(partnersListData) == len(test_partners_data)


async def test_get_one_partner(ac: AsyncClient):
  partnerData = await ac.get('/partners/1')
  assert partnerData.status_code == 200
  partnerDataJson = partnerData.json()
  partner = partner_schemas.PartnerBaseShow(**partnerDataJson)
  assert partner.title == test_partners_data[0]['title']



async def test_create_partner_service(ac: AsyncClient):
  for indx, item in enumerate(test_partner_service_data):
    partner_service = await ac.post('/partners/partner_service/', json=item)
    assert partner_service.status_code == 201
    partnerServiceJson = partner_service.json()
    partnerSericeCreatedData = partner_schemas.PartnerServiceBaseResponse(**partnerServiceJson)
    assert partnerSericeCreatedData.service_name == test_partner_service_data[indx]['service_name']



async def test_create_partner_with_service(ac: AsyncClient):
  for indx, item in enumerate(test_partner_and_services_data):
    partnerBankData = await ac.post('/partners/partner_with_service/', json=item)
    assert partnerBankData.status_code == 201
    partnerBankDataJson = partnerBankData.json()
    partner_bank = partner_schemas.CreatePartnerAndServiceResponse(**partnerBankDataJson)
    assert partner_bank.title == item['title']
    # assert partner_bank.bank_account.account_number == item['bank_account']['account_number']
    assert len(partner_bank.partner_services) == len(test_partner_and_services_data[indx]['partner_services'])



async def test_create_partner_bank(ac: AsyncClient):
  for indx, item in enumerate(test_partner_bank_data):
    partnerBank = await ac.post('/partners/partner_bank/', json=item)
    assert partnerBank.status_code == 201
    partnerBankJson = partnerBank.json()
    bank_data = partner_schemas.BankAccountShowBase(**partnerBankJson)
    assert bank_data.account_number == test_partner_bank_data[indx]['account_number']
    assert bank_data.bank_name == test_partner_bank_data[indx]['bank_name']







# async def test_get_partner_services_and_bank(ac: AsyncClient):...

# async def test_get_partner_with_service_and_bank(ac: AsyncClient):
#   partnerBankData = await ac.get('/partners/partner_with_bank/6',)
#   assert partnerBankData.status_code == 200
#   partnerBankDataJson = partnerBankData.json()
#   partner_bank = partner_schemas.PartnerBankCreateResponse(**partnerBankDataJson)
#   assert partner_bank.title == test_partner_with_bank_data[0]['title']
#   assert partner_bank.bank_account.account_number == test_partner_with_bank_data[0]['bank_account']['account_number']