import React from 'react';

import { MainMenu, MainProgramComponent } from '../../modules';


export default function ProgramPage() {
  return(
    <div className="container program">
      <MainMenu />
      <MainProgramComponent />
    </div>
  );
}