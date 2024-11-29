import React from 'react';
import { useParams } from 'react-router-dom';

import style from './styles/hotel_profile_main.module.css'
import HotelProfileData from './HotelProfileData';
import HotelProfileInfo from './HotelProfileInfo';


export default function HotelProfileMainComponent() {
  const {hotelId} = useParams()

  return(
    <section className={style.hoteProfileMainContainer}>
      <h2>Hotel Profile {hotelId}</h2>
      <div className={style.hotelDataContainers}>
        <HotelProfileData />
        <HotelProfileInfo />
      </div>
    </section>
  );
}