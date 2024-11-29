import React from 'react';


import style from './styles/hotel_profile_data.module.css'


import { ProfileInput } from '../../../../ui';



export default function HotelProfileData() {
  
  return(
    <>
      <section className={style.hotelProfile}>
        <div className={style.hotelData}>
          <div className={style.hotelDataHeader}>
            <h4>{hotelData.name}</h4>
          </div>
          <div className={style.hotelInfo}>
            <h6>Информация проживания</h6>
            <ProfileInput
            fieldTitle='Город'
            fieldData={hotelData.city}
            />
            <ProfileInput
            fieldTitle='Адрес'
            fieldData={hotelData.address}
            />
            <ProfileInput
            fieldTitle='Телефон'
            fieldData={hotelData.contacts}
            />
            <ProfileInput
            fieldTitle='Почта'
            fieldData={hotelData.email}
            />
          </div>
          <div className={style.hotelDesc}>
            <h6>Описание отеля</h6>
            <p>{hotelData.desc}</p>
          </div>
        </div>
      </section>
    </>

  );
}


const hotelData = {
  'id': 1,
  "name": "Отель Измайлово Бета",
  "address": "Измайловское шоссе, 71, корпус 2Б",
  "contacts": "777-96-85",
  "desc": "Доступный трехвездочный бизнес-отель в зеленом районе города, входит в гостиничный комплекс «Измайлово». Расположен недалеко от метро «Партизанская», станции МЦК «Измайлово» и Измайловского парка – одного из самых больших в Москве.",
  "city": "Москва",
  "email": "hotel@mail.ru"
}