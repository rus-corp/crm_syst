import { backend } from "../_variables";

export const getClientProgramPayments = async (clientProgramId) => {
  try {
    const response = await backend.get(
      `/payments/${clientProgramId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const createClientProgramPayment = async (paymentData) => {
  try {
    const response = await backend.post(
      '/payments/',
      paymentData
    )
    return response
  } catch (error) {
    console.error(error)
  }
}