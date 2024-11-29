import React from 'react';

import { MainMenu, HotelMainComponent } from '../../modules';
import { Outlet, useLocation } from 'react-router-dom';

export default function HotelPage() {
  const location = useLocation()

  const isHotelProfile = location.pathname.includes('/hotels/') && location.pathname !== '/hotels'
  return(
    <div className="container hotels">
      <MainMenu />
      {/* {isHotelProfile ? <Outlet /> : <HotelMainComponent />} */}
      {/* <HotelMainComponent /> */}
      <Outlet />
    </div>
  );
}