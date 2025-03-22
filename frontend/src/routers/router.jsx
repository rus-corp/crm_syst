import { createBrowserRouter } from "react-router-dom";


import { CrmPage, HotelPage, ClientPage,
  CreateProgramPage, CompanyPage,
  CreateItemPage, ProgramPage,
  BlockItemPage, PartnerPage } from "../pages";

  import { HotelMainComponent, CreateHotel,
  CreateRoom, CreatePartner, 
  PartnerMain, PartnerProfileComponent, HotelProfileMainComponent,
  ClientProfile, ClientMainListComponent, CreateProgramComponent, 
  ProgramExpenses, AppendHotels}
  from "../modules";




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
    path: '/partners',
    element: <PartnerPage />,
    children: [
      {
        path: '',
        element: <PartnerMain />
      },
      {
        path: 'create_partner',
        element: <CreatePartner />
      },
      {
        path: ':partnerId',
        element: <PartnerProfileComponent />
      }
    ]
  },
  {
    path: '/company',
    element: <CompanyPage />,
  },
  {
    path: '/company/:type',
    element: <BlockItemPage />
  },
  {
    path: '/create_item/:type',
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