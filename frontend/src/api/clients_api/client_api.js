import { backend } from "../_variables";


export const getClientList = async() => {
  try {
    const response = await backend.get(
      '/clients/base/'
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getClientDataWithProgram = async (clientSlug) => {
  try {
    const response = await backend.get(
      `/clients/base/program_profile_doc/${clientSlug}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}

export const getClientBySlug = async(clientSlug) => {
  try {
    const response = await backend.get(
      `/clients/${clientSlug}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const createClient = async (clientData) => {
  try {
    const response = await backend.post(
      '/clients/',
      clientData
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getClientCurrentProgram = async (clientSlug) => {
  try {
    const response = await backend.get(
      `/clients/program/${clientSlug}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}