import { appendClientToProgramRoom } from "./client_program_room/clientProgramRoom";
import { 
  createClient,
  getClientBySlug,
  getClientCurrentProgram,
  getClientProfileAndDoc,
  getClientList,
  updateClientMainData,
  updateClientProfileData,
  appendClientToProgram,
 } from "./clients_api/client_api";

import {
  createHotel,
  getHotels,
  getHotelByIdWithRooms,
  updateHotelProfileById,
  getHotelsWithoutRooms,
  appendHotelRoomToProgram
} from "./hotels_api/hotels";

import { createRoomsList, getProgramRoomClient } from "./hotels_api/rooms";

import {
  appendPartnerRoProgramReq,
  createPartner,
  deletePartnerById,
  getPartnerById,
  getPartnerByIdWithServiceAndBank,
  getPartnersFilterList,
  updatePartnerById
} from "./partners/partners_api";

 import { 
  createClientProgramPayment,
  getClientProgramPayments
 } from "./payments_api/api";

import { getProgramClients,
  getProgramHotelRooms,
  getPrograms,
  createProgram, 
  getProgramExpenses,
  getProgramPartners,
  createProgramPrices,
  getProgramPrices}
  from "./programs_api/programs_api";

import {
  createCostItem,
  createExpenseItem,
  createProgramExpenses,
  createStaffItem,
  getCostItemsList,
  getEmployeePositions,
  getExpensesList,
  getStaffs
} from "./staff_api/staff_api";





export { getPrograms, getProgramClients, getProgramHotelRooms,
  getClientList, getClientBySlug, createClient,
  getClientCurrentProgram, getClientProfileAndDoc,
  createClientProgramPayment, getClientProgramPayments,
  createHotel, getHotels, getHotelByIdWithRooms, createRoomsList,
  updateHotelProfileById, createProgram, createStaffItem, getStaffs,
  getExpensesList, getEmployeePositions, createExpenseItem,
  createCostItem, getCostItemsList, getHotelsWithoutRooms,
  appendHotelRoomToProgram, getPartnersFilterList, getPartnerById,
  createPartner, updatePartnerById, deletePartnerById,
  updateClientMainData, updateClientProfileData, createProgramExpenses,
  getPartnerByIdWithServiceAndBank, appendPartnerRoProgramReq,
  getProgramExpenses, getProgramPartners, createProgramPrices,
  getProgramPrices, appendClientToProgram, getProgramRoomClient,
  appendClientToProgramRoom
 }