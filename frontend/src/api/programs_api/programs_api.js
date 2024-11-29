import { backend } from "../_variables";


export const getPrograms = async () => {
  try {
    const response = await backend.get(
      `/programs/`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const createProgram = async(programData) =>{
  try {
    const response = await backend.post(

    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getProgramItem = async(programSlug) => {
  try {
    const response = await backend.get(

    )
    return response
  } catch (error) {
    console.error(error)
  }
}

export const getProgramClients = async(programId) => {
  try {
    const response = await backend.get(
      `/programs/clients/${programId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getProgramHotels = async(programSlug) => {
  try {
    const response = await backend.get(
      `programs/${programSlug}/hotels`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


