import { backend } from "../_variables";

export const getStaffs = async (limit=null) => {
  let url;
  if (limit) {
    url = `/staff/employee/employee_expenses/?limit=${limit}`
  } else {
    url = '/staff/employee/employee_expenses/'
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



export const getExpensesList = async () => {
  try {
    const response = await backend.get(
      '/staff/expenses/'
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



