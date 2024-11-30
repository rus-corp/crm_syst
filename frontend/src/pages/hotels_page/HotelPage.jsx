import React from 'react';

import { MainMenu, HotelMainComponent } from '../../modules';
import { Outlet, useLocation } from 'react-router-dom';

export default function HotelPage() {
  const location = useLocation()
  return(
    <div className="container hotels">
      <MainMenu />
      <Outlet />
    </div>
  );
}