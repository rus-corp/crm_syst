import React from 'react';

import style from '../../styles/create_partner.module.css'
import { CreateItemInput } from '../../../../ui';



export default function CreatePartnerService({
  itemIndx,
  serviceData,
  handleChange
}) {
  const handleChangeData = (name, value) => {
    handleChange(itemIndx, name, value)
  }
  return(
    <div className={style.serviceItem}>
      <div className={style.fieldItem}>
        <CreateItemInput
        fieldTitle={'Название услуги'}
        value={serviceData.service_name}
        fieldName={'service_name'}
        changeFunc={handleChangeData}
        />
      </div>
      <div className={style.fieldItem}>
        <CreateItemInput
        fieldTitle={'Стоимость'}
        value={serviceData.price}
        fieldName={'price'}
        changeFunc={handleChangeData}
        />
      </div>
    </div>
  );
}