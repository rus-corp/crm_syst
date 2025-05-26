import { authBackend } from "../_variables";


export const authLogin = async (params) => {
  try {
    const response = await authBackend.post(
      '/auth/login/', 
      params,
      {headers:
        {'Content-Type': 'application/x-www-form-urlencoded'}
      })
      if (response.status === 201) {
        return response
      } else {
        return response.status
      }
  } catch(error) {
    return error.response.status
  }
}