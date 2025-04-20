import { backend } from "../_variables";


export const getPrograms = async () => {
  try {
    const response = await backend.get(
      '/program/base/'
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const createProgram = async(programData) =>{
  try {
    const response = await backend.post(
      '/program/base/',
      programData
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
      `/programs/base/clients/${programId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getProgramHotelRooms = async(programId) => {
  try {
    const response = await backend.get(
      `/program/base/program_hotels/${programId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getProgramExpenses = async (programId) => {
  try {
    const response = await backend.get(
      `/program/base/program_expenses/${programId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getProgramPartners = async (programId) => {
  try {
    const response = await backend.get(
      `/program/base/program_partners/${programId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const createProgramPrices = async(programId) => {
  try {
    const response = await backend.post(
      `/program/price/${programId}`
    )
    return response
  } catch (error) {
    return error.response
  }
}

export const getProgramPrices = async (programId) => {
  try {
    const response = await backend.get(
      `/program/price/${programId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}