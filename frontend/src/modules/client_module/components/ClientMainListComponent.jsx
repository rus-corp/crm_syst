import React from 'react';
import { useParams } from 'react-router-dom';

import style from './client_module.module.css'
import ClientProfile from './client_profile/ClientProfile';
import ClientProgram from './client_profile/ClientProgram';

import { getClientBySlug } from '../../../api';



export default function ClientMainListComponent() {


  return(
    <section className={style.clientSection}>
      <h2>Список клиентов</h2>
    </section>
  );
}