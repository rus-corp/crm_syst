import { backend } from "../_variables";


export const createHotel = async (hotelData) => {
  try {
    const response = await backend.post(
      '/hotels/',
      hotelData
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getHotels = async () => {
  try {
    const response = await backend.get(
      '/hotels/'
    )
    return response
  } catch (error) {
    console.error(error)
  }
}

export const getHotelById = async (hotelId) => {
  try {
    const response = await backend.get(
      `/hotels/${hotelId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}