import { backend } from "../_variables";


export const createRoomsList = async (roomsDataList) => {
  try {
    const response = await backend.post(
      '/rooms/room_list/',
      roomsDataList
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const getProgramRoomClient = async (programRoomId) => {
  try {
    const response = await backend.get(
      `/program_rooms/${programRoomId}`,
    )
    return response
  } catch (error) {
    console.error(error)
  }
}