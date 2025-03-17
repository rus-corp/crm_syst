import { backend } from "../_variables";


export const getPartnersFilterList = async (categoryData) => {
  try {
    const response = await backend.get(`/partners/?category=${categoryData}`);
    return response
  } catch (error) {
    console.error(error);
  }
}


export const createPartner = async (partnerData) => {
  try {
    const response = await backend.post('/partners/partner_with_service/', partnerData);
    return response
  } catch (error) {
    return error.response
  }
}


export const getPartnerById = async (partnerId) => {
  try {
    const response = await backend.get(`/partners/${partnerId}`);
    return response
  } catch (error) {
    console.error(error);
  }
}

export const updatePartnerById = async (partnerId, partnerData) => {
  try {
    const response = await backend.patch(`/partners/${partnerId}`, partnerData);
    return response
  } catch (error) {
    return error.response
  }
}

export const deletePartnerById = async (partnerId) => {
  try {
    const response = await backend.delete(`/partners/${partnerId}`);
    return response
  } catch (error) {
    return error.response
  }
}