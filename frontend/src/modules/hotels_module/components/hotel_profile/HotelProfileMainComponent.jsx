import React from 'react';
import { useParams } from 'react-router-dom';

import style from './styles/hotel_profile_main.module.css'
import HotelProfileData from './HotelProfileData';
import HotelProfileInfo from './HotelProfileInfo';

import { getHotelByIdWithRooms } from '../../../../api';

export default function HotelProfileMainComponent() {
  const { hotelId } = useParams()
  const [hotelProfile, setHotelProfile] = React.useState({
    "title": "",
    "address": "",
    "contacts": "",
    "city": "",
    "email": "",
    "desc": "",
    "id": hotelId,
    "rooms": []
  })
  const handleChange = (ev) => {
    const { name, value } = ev.target
    setHotelProfile((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const getHotelData = async (hotelProfileId) => {
    const response = await getHotelByIdWithRooms(hotelProfileId)
    if (response.status === 200) {
      setHotelProfile(response.data)
    }
  }

  React.useEffect(() => {
    if (hotelId !== 0) {
      getHotelData(hotelId)
    }
  }, [hotelId])

  return(
    <section className={style.hoteProfileMainContainer}>
      <h2>Hotel Profile {hotelProfile.title}</h2>
      <div className={style.hotelDataContainers}>
        <HotelProfileData
        hotelId={hotelId}
        hotelTitle={hotelProfile.title}
        hotelCity={hotelProfile.city}
        hotelEmail={hotelProfile.email}
        hotelAddress={hotelProfile.address}
        hotelContacts={hotelProfile.contacts}
        hotelDesc={hotelProfile.desc}
        handleChangeFunc={handleChange}
        />
        <HotelProfileInfo
        hotelRooms={hotelProfile.rooms}
        />
      </div>
    </section>
  );
}
