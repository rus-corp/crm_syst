import React from 'react';
import { Outlet, useLocation } from 'react-router-dom';


import { MainMenu } from '../../modules';

export default function ClientPage() {
  return(
    <div className="container hotels">
      <MainMenu />
      <Outlet />
    </div>
  );
}