import { createBrowserRouter } from "react-router-dom";


import { CrmPage, HotelPage, ClientPage, CreateProgramPage, CompanyPage, CreateItemPage, ProgramPage } from "../pages";
import { HotelMainComponent, CreateHotel, CreateRoom } from "../modules";
import HotelProfileMainComponent from "../modules/hotels_module/components/hotel_profile/HotelProfileMainComponent";
import { ClientProfile, ClientMainListComponent } from "../modules/client_module";
import {CreateProgramComponent} from "../modules/program_module";
import { ProgramExpenses, AppendHotels } from "../modules/program_module";



export const router = createBrowserRouter([
  {
    path: '/',
    element: <CrmPage />
  },
  {
    path: '/programs',
    element: <ProgramPage />
  },
  {
    path: '/create_program',
    element: <CreateProgramPage />,
    children: [
      {
        path: '',
        element: <CreateProgramComponent />
      },
      {
        path: 'add_hotel',
        element: <AppendHotels />
      },
      {
        path: 'add_expenses',
        element: <ProgramExpenses />
      },
    ]
  },
  {
    path: '/clients',
    element: <ClientPage />,
    children: [
      {
        path: '',
        element: <ClientMainListComponent />
      },
      {
        path: ':clientSlug',
        element: <ClientProfile />
      }
    ]
  },
  {
    path: '/hotels',
    element: <HotelPage />,
    children: [
      {
        path: '',
        element: <HotelMainComponent />
      },
      {
        path: ':hotelId',
        element: <HotelProfileMainComponent />
      },
      {
        path: 'create_hotel',
        element: <CreateHotel />
      },
      {
        path: 'create_hotel_rooms',
        element: <CreateRoom />
      }
    ]
  },
  {
    path: '/company',
    element: <CompanyPage />,
  },
  {
    path: '/company/:type',
    element: <CreateItemPage />
  }
], {
  future: {
    v7_startTransition: true,
    v7_relativeSplatPath: true,
    v7_fetcherPersist: true,
    v7_normalizeFormMethod: true,
    v7_skipActionErrorRevalidation: true,
    v7_partialHydration: true
  }
})