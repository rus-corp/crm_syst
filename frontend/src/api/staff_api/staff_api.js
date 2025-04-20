import { backend } from "../_variables";

export const getStaffs = async (limit=null) => {
  let url;
  if (limit) {
    url = `/staff/employee/?limit=${limit}`
  } else {
    url = '/staff/employee/'
  }
  try {
    const response = await backend.get(
      url
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const createStaffItem = async (staffData) => {
  try {
    const response = await backend.post(
      '/staff/employee/',
      staffData
    )
    return response
  } catch(error) {
    return error.response
  }
}



export const getExpensesList = async (limit=null) => {
  let url;
  if (limit) {
    url = `/staff/expenses/?limit=${limit}`
  } else {
    url = '/staff/expenses/'
  }
  try {
    const response = await backend.get(
      url
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getEmployeePositions = async () => {
  try {
    const response = await backend.get('/staff/employee/position_list/')
    return response
  } catch(error) {
    console.error(error)
  }
}


export const createExpenseItem = async (expenseData) => {
  try {
    const response = await backend.post(
      '/staff/expenses/',
      expenseData
    )
    return response
  } catch (error) {
    return error.response
  }
}


export const createCostItem = async (costItemData) => {
  try {
    const response = await backend.post(
      '/staff/cost_items/',
      costItemData
    )
    return response
  } catch (error) {
    return error.response
  }
}


export const getCostItemsList = async () => {
  try { 
    const response = await backend.get(
      '/staff/cost_items/'
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const createProgramExpenses = async (expenseData) => {
  try {
    const response = await backend.post(
      '/staff/expenses/create_static_and_employee_expense/',
      expenseData
    )
    return response
  } catch (error) {
    return error.response
  }
}