import React from 'react';
import { useNavigate } from 'react-router-dom';

import style from './create_hotel.module.css'
import {
  CreateItemInput,
  SaveBtnComponent,
  TextAreaComponent,
  NotificationComponent
} from '@/ui';
import { createHotel } from '@/api';

export default function CreateHotel() {
  const navigation = useNavigate()
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const [hotelData, setHotelData] = React.useState({
    title: '',
    address: '',
    contacts: '',
    city: '',
    email: '',
    desc: ''
  })

  const handleCreateHotel = async (createdData) => {
    const response = await createHotel(createdData)
    if (response.status === 201) {
      setAlert({severity: 'success', message: 'Отель успешно добавлен'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
        navigation('/hotels/create_hotel_rooms')
      }, 1500);
    } else if(response.status === 403) {
      setAlert({severity: 'error', message: response.message})
    }
  }

  const handleSubmit = async () => {
    handleCreateHotel(hotelData)
  }

  const handleChangeField = (name, value) => {
    setHotelData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  return(
    <section className={style.createHotel}>
      <div className={style.createHotelData}>
        <div className={style.sectionHeader}>
          <h2>Создать отель</h2>
          <NotificationComponent
          severity={alert.severity}
          message={alert.message}
          />
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
          <div className={style.createdField}>
            <TextAreaComponent
            fieldTitle='Описание'
            fieldName='desc'
            value={hotelData.desc}
            handleChange={handleChangeField}
            />
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