import React from 'react';

import style from './styles/client_profile_data.module.css'
import { ProfileInput } from '../../../../ui';
import { formatedClientStatus } from '../../../../utils';


export default function ClientProfileData({ clientProfile }) {
  const clientStatus = formatedClientStatus(clientProfile?.profile?.status)
  return(
    <section className={style.clientProfile}>
      <div className={style.clientFio}>
        <div className={style.clientProfileHeader}>
          <h3>{clientProfile?.last_name}</h3>
          <h3>{clientProfile?.name}</h3>
        </div>
        <h6>{clientProfile?.second_name}</h6>
        <div className={style.clientCreated}>
          <p>Дата регистрации:</p>
          <p>{clientProfile?.created_at.slice(0, 10)}</p>
        </div>
        <div className="clientStatus">
          <p>Статус Клиента</p>
          <h6>{clientStatus}</h6>
        </div>
      </div>
      <div className={style.clientMainInfo}>
        <h5>Информация</h5>
        <ProfileInput
        fieldTitle="Город"
        fieldData={clientProfile?.profile?.city}
        />
        <ProfileInput 
        fieldTitle="Телефон"
        fieldData={clientProfile?.phone}
        />
        <ProfileInput 
        fieldTitle="Email"
        fieldData={clientProfile?.email}
        />
        <ProfileInput 
        fieldTitle="Дата рождения"
        fieldData={clientProfile?.profile?.date_of_birth}
        />
        <ProfileInput 
        fieldTitle="Питание"
        fieldData={clientProfile?.profile?.nutrition_features}
        />
        <ProfileInput 
        fieldTitle="Размер футболки"
        fieldData={clientProfile?.profile?.shirt_size}
        />
        <ProfileInput 
        fieldTitle="Комментарий"
        fieldData={clientProfile?.profile?.comment}
        />
      </div>
    </section>
  );
}