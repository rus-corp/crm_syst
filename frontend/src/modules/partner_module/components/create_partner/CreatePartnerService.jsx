import React from 'react';
import Checkbox from '@mui/material/Checkbox';


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

  const handleChangeCheckbox = (event) => {
    const { name, checked } = event.target;
    handleChange(itemIndx, name, checked);
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
      <div className={style.fieldItem}>
        <p>Цена за группу</p>
        <Checkbox
        defaultChecked
        sx={{ '& .MuiSvgIcon-root': { fontSize: 28 } }}
        inputProps={{ 'aria-label': 'controlled' }}
        onChange={handleChangeCheckbox}
        name='service_type'
        value={serviceData.service_type}
        />
      </div>
    </div>
  );
}