import React from 'react';

import style from '../../styles/create_partner.module.css'
import { CreateItemInput } from '../../../../ui';



export default function CreatePartner() {
  const [partnerData, setPartnerData] = React.useState({
    title: '',
    law_title: '',
    price: '',
    contract_number: '',
    bank_account: '',
  })
  return(
    <section className={style.createHotel}>
          <div className={style.createHotelData}>
            <div className={style.sectionHeader}>
              <h2>Создать отель</h2>
            </div>
            <div className={style.sectionCreateData}>
              <div className={style.createdField}>
                <CreateItemInput
                fieldTitle='Название Отеля'
                fieldType='text'
                fieldName='title'
                value={hotelData.title}
                changeFunc={handleChangeField}
                />
              </div>
              <div className={style.flexFields}>
                <div className={style.createdField}>
                  <CreateItemInput
                  fieldTitle='Адрес'
                  fieldType='text'
                  fieldWidth='93%'
                  fieldName='address'
                  value={hotelData.address}
                  changeFunc={handleChangeField}
                  />
                </div>
                <div className={style.createdField}>
                  <CreateItemInput
                  fieldTitle='Контакты'
                  fieldType='text'
                  fieldWidth='93%'
                  fieldName='contacts'
                  value={hotelData.contacts}
                  changeFunc={handleChangeField}
                  />
                </div>
              </div>
              <div className={style.flexFields}>
                <div className={style.createdField}>
                  <CreateItemInput
                  fieldTitle='Город'
                  fieldType='text'
                  fieldWidth='93%'
                  fieldName='city'
                  value={hotelData.city}
                  changeFunc={handleChangeField}
                  />
                </div>
                <div className={style.createdField}>
                  <CreateItemInput
                  fieldTitle='Email'
                  fieldType='email'
                  fieldWidth='93%'
                  fieldName='email'
                  value={hotelData.email}
                  changeFunc={handleChangeField}
                  />
                </div>
              </div>
              <div className={style.saveBtn}>
                <SaveBtnComponent
                saveTitle='Отель'
                clicked={handleSubmit}
                />
              </div>
            </div>
          </div>
        </section>
  );
}