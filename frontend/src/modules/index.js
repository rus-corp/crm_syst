import { ClientMainListComponent, ClientProfile } from "./client_module";
import CompanyMain from "./company_module/CompanyMain";
import ExpenseBlock from "./company_module/expenses/ExpenseItem";
import StaffBlock from "./company_module/staff/StaffItem";
import CreateHotel from "./hotels_module/components/create_hotel/CreateHotel";
import CreateRoom from "./hotels_module/components/create_hotel/CreateRoom";
import HotelProfileMainComponent from "./hotels_module/components/hotel_profile/HotelProfileMainComponent";
import HotelMainComponent from "./hotels_module/components/HotelMainComponent";
import MainMenu from "./page_menu_section/MainMenu";
import CreatePartner from "./partner_module/components/create_partner/CreatePartner";
import PartnerMain from "./partner_module/components/PartnerMain";
import PartnerProfileComponent from "./partner_module/components/PartnerProfileComponent";
import { AppendHotels, CreateProgramComponent, ProgramExpenses, ProgramServices } from "./program_module";
import TotalProgramComponent from "./program_module/components/create_program/TotalProgramComponent";
import MainProgramComponent from "./program_module/components/MainProgramComponent";

export { MainMenu, HotelMainComponent,
  MainProgramComponent, CreateHotel,
  CreateRoom, CompanyMain, StaffBlock, ExpenseBlock,
  PartnerMain, CreatePartner, PartnerProfileComponent,
  HotelProfileMainComponent, ClientProfile,
  ClientMainListComponent, CreateProgramComponent,
  ProgramExpenses, AppendHotels, ProgramServices, TotalProgramComponent
 }