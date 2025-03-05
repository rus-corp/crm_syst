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


// {
//   "title": "Отель Измайлово Гамма",
//   "address": "Измайловское шоссе, д.71, корп. 4Г-Д",
//   "contacts": "777-84-21",
//   "city": "Мурманск",
//   "email": "gamma@mail.ru",
//   "desc": "Отель «Гамма Измайлово» является частью легендарного гостиничного комплекса на 2000 номеров в районе Измайлово, в 600 м от большого парка. До метро «Партизанская» ― 6 минут ходьбы, до метро «Измайлово» ― 7 минут. За 15 минут на транспорте можно добраться до ",
//   "id": 2,
//   "rooms": [
//       {
//           "id": 1,
//           "room_type": "Трехместный номер",
//           "room_price": 2600,
//           "room_volume": 3
//       },
//       {
//           "id": 11,
//           "room_type": "Трехместный номер",
//           "room_price": 6900,
//           "room_volume": 3
//       },
//       {
//           "id": 12,
//           "room_type": "Трехместный номер",
//           "room_price": 1700,
//           "room_volume": 3
//       },
//       {
//           "id": 21,
//           "room_type": "Трехместный номер",
//           "room_price": 5400,
//           "room_volume": 3
//       },
//       {
//           "id": 25,
//           "room_type": "Двухместный номер",
//           "room_price": 4200,
//           "room_volume": 2
//       },
//       {
//           "id": 28,
//           "room_type": "Двухместный номер",
//           "room_price": 4700,
//           "room_volume": 2
//       }
//   ],
//   "hotel_rooms_volume": 16
// }