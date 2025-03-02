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

export const getHotelsWithoutRooms = async () => {
  try {
    const response = await backend.get('/hotels')
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getHotels = async () => {
  try {
    const response = await backend.get(
      '/hotels/with_rooms/'
    )
    return response
  } catch (error) {
    console.error(error)
  }
}

export const getHotelByIdWithRooms = async (hotelId) => {
  try {
    const response = await backend.get(
      `/hotels/with_rooms/${hotelId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const updateHotelProfileById = async (hotelId, hotelData) => {
  try {
    const response = await backend.patch(
      `/hotels/${hotelId}`,
      hotelData
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const appendHotelRoomToProgram = async (data) => {
  try {
    const response = await backend.post(
      '/hotels/room_to_program/',
      data
    )
    return response
  } catch (error) {
    return error.response
  }
}