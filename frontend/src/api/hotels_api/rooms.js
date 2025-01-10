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

