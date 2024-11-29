import React from 'react';

import style from './styles/crm_page.module.css'

import { MainMenu } from '../../modules';
import { CrmTable } from '../../modules/crm_module';




export default function CrmPage() {
  return(
    <div className="container">
      <div className={style.crmPage}>
      <MainMenu />
      <CrmTable />
      </div>
    </div>
  );
}