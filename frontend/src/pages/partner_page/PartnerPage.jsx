import React from 'react';
import { MainMenu } from '../../modules';
import { Outlet } from 'react-router-dom';

export default function PartnerPage() {
  return(
    <div className="container program">
      <MainMenu />
      <Outlet />
    </div>
  );
}