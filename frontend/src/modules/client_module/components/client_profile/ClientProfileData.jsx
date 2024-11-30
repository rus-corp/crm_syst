import React from 'react';

import style from './styles/client_profile_data.module.css'
import { ProfileInput } from '../../../../ui';

export default function ClientProfileData({props}) {
  return(
    <section className={style.clientProfile}>
      <div className={style.clientFio}>
        <div className={style.clientProfileHeader}>
          <h3>{props?.last_name}</h3>
          <h3>{props?.name}</h3>
        </div>
        <h6>{props?.second_name}</h6>
        <div className={style.clientCreated}>
          <p>Дата регистрации:</p>
          <p>{props?.created_at.slice(0, 10)}</p>
        </div>
      </div>
      <div className={style.clientMainInfo}>
        <h5>Информация</h5>
        <ProfileInput
        fieldTitle="Город"
        fieldData={props?.profile?.city}
        />
        <ProfileInput 
        fieldTitle="Телефон"
        fieldData={props?.phone}
        />
        <ProfileInput 
        fieldTitle="Email"
        fieldData={props?.email}
        />
        <ProfileInput 
        fieldTitle="Дата рождения"
        fieldData={props?.profile?.date_of_birth}
        />
      </div>
    </section>
  );
}