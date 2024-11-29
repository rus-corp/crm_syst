import { createBrowserRouter } from "react-router-dom";


import { CrmPage, HotelPage, ClientPage } from "../pages";
import ProgramPage from "../pages/program_page/ProgramPage";
import { HotelMainComponent } from "../modules";
import HotelProfileMainComponent from "../modules/hotels_module/components/hotel_profile/HotelProfileMainComponent";





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
    path: '/clients',
    element: <ClientPage />
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
      }
    ]
  },
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