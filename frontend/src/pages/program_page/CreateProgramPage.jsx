import React from 'react';

// import style from './'
import { Outlet } from 'react-router-dom';
import { MainMenu } from '../../modules';
import { CreateProgramComponent } from '../../modules/program_module';

export default function CreateProgramPage() {
  return(
    <div className="container program">
      <MainMenu />
      <Outlet />
    </div>
  );
}