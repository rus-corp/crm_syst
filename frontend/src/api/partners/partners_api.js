import { backend } from "../_variables";


export const getPartnersFilterList = async (categoryData) => {
  let url;
  if (categoryData) {
    url = `/partners/?category=${categoryData}`
  }else {
    url = '/partners/'
  }
  try {
    const response = await backend.get(url);
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


export const getPartnerByIdWithServiceAndBank = async (partnerId) => {
  try {
    const response = await backend.get(
      `/partners/partner_with_service_and_bank/${partnerId}`
    )
    return response
  } catch (error) {
    console.error(error)
  }
}


export const appendPartnerRoProgramReq = async (partnerData) => {
  try {
    const response = await backend.post(
      '/partners/append_partner_to_program/',
      partnerData
    )
    return response
  } catch (error) {
    return error.response
  }
}