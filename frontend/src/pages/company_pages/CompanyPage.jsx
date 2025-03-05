import React from 'react';
import { MainMenu } from '../../modules';
import { CompanyMain } from '../../modules';


export default function CompanyPage() {
  return(
    <div className="container program">
      <MainMenu />
      <CompanyMain />
    </div>
  );
}