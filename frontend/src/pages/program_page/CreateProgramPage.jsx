import React from 'react';

// import style from './'

import { MainMenu } from '../../modules';
import { CreateProgramComponent } from '../../modules/program_module';

export default function CreateProgramPage() {
  return(
    <div className="container program">
      <MainMenu />
      <CreateProgramComponent />
    </div>
  );
}