import { backend } from "../_variables";



export const appendClientToProgramRoom = async (roomData) => {
  try {
    const response = await backend.post(
      '/clients/base/append_client_to_prog_room/',
      roomData,
    )
    return response
  } catch (error) {
    console.error(error)
  }
}

export const deleteClientFromProgramRoom = async (roomData) => {
  try {
    const response = await backend.post(
      '/clients/base/delete_client_from_prog_room/',
      roomData,
    )
    return response
  } catch (error) {
    console.error(error)
  }
}