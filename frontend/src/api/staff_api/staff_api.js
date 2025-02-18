import { backend } from "../_variables";

export const getStaffs = async (limit = null) => {
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


export const createStaffItem = async (data) => {
  try {
    const response = await backend.post(
      '/staff/employee/',
      data
    )
    return response
  } catch(error) {
    console.error(error)
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



