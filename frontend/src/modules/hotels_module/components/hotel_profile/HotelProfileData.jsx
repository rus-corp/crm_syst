import React from 'react';


import style from './styles/hotel_profile_data.module.css'


import { ProfileInput, TextAreaComponent, NotificationComponent } from '../../../../ui';
import { updateHotelProfileById } from '../../../../api';


export default function HotelProfileData({
  hotelId,
  hotelTitle,
  hotelCity,
  hotelEmail,
  hotelAddress,
  hotelContacts,
  hotelDesc,
  handleChangeFunc
}) {
  const [profileUpdateData, setProfileUpdateData] = React.useState({
    city: null,
    address: null,
    contacts: null,
    email: null,
    desc: null,
  })
  const [alert, setAlert] = React.useState({severity:'', message:''})
  const updateHotel = async(hotelProfileId, updatedData) => {
    const response = await updateHotelProfileById(hotelProfileId, updatedData)
    if (response.status === 200) {
      setAlert({severity: 'success', message: 'Данные обновлены'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
      }, 2500);
    }
  }

  const handleChange = (ev) => {
    const { name, value } = ev.target
    handleChangeFunc(ev)
    setProfileUpdateData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleKeyDown = (ev) => {
    if (ev.key === 'Enter') {
      console.log(profileUpdateData)
      updateHotel(hotelId, profileUpdateData)
    }
  }

  return(
    <>
      <section className={style.hotelProfile}>
        <div className={style.hotelData}>
          <div className={style.hotelDataHeader}>
            <h4>{hotelTitle}</h4>
          </div>
          <div className={style.hotelInfo}>
            <h6>Информация проживания</h6>
            <NotificationComponent
            severity={alert.severity}
            message={alert.message}
            />
            <ProfileInput
            fieldName='city'
            fieldType='text'
            fieldTitle='Город'
            fieldData={hotelCity}
            handleChange={handleChange}
            handleKeyDown={handleKeyDown}
            />
            <ProfileInput
            fieldName='address'
            fieldType='text'
            fieldTitle='Адрес'
            fieldData={hotelAddress}
            handleChange={handleChange}
            handleKeyDown={handleKeyDown}
            />
            <ProfileInput
            fieldName='contacts'
            fieldType='text'
            fieldTitle='Телефон'
            fieldData={hotelContacts}
            handleChange={handleChange}
            handleKeyDown={handleKeyDown}
            />
            <ProfileInput
            fieldName='email'
            fieldType='email'
            fieldTitle='Почта'
            fieldData={hotelEmail}
            handleChange={handleChange}
            handleKeyDown={handleKeyDown}
            />
          </div>
          <div className={style.hotelDesc}>
            <h6>Описание отеля</h6>
            <TextAreaComponent
            fieldTitle={hotelTitle}
            fieldName='desc'
            fieldData={hotelDesc}
            handleChange={handleChange}
            handleKeyDown={handleKeyDown}
            />
          </div>
        </div>
      </section>
    </>
  );
}