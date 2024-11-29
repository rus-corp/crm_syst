import React from 'react';

import { ThreeComponentSwitch } from '@/ui';
import style from './styles/hotel_profile_info.module.css'
import HotelRoom from '../hotel_rooms/HotelRoom';

export default function HotelProfileInfo() {
  return(
    <div className={style.hotelProfileInfoContainer}>
      <ThreeComponentSwitch />
      <div className={style.hotelRooms}>
        {hotelRooms.map((room) => (
          <HotelRoom key={room.id}
          roomType={room.room_type}
          roomPrice={room.room_price}
          roomVolume={room.room_volume}
          />
        ))}
      </div>
    </div>
  );
}


const hotelRooms = [
  {
    "id": 1,
    "room_type": "Стандарт ДвухМестный",
    "room_price": "4300",
    "room_volume": "2",
    "hotel": "1",
  },
  {
    "id": 2,
    "room_type": "Стандарт Одноместный",
    "room_price": "2300",
    "room_volume": "2",
    "hotel": "1",
  },
  {
    "id": 3,
    "room_type": "Стандарт ДвухМестный + доп.кровать",
    "room_price": "4600",
    "room_volume": "2",
    "hotel": "1",
  },
  {
    "id": 4,
    "room_type": "Стандарт ДвухМестный личный душ",
    "room_price": "5300",
    "room_volume": "2",
    "hotel": "1",
  },
  {
    "id": 5,
    "room_type": "Стандарт ДвухМестный Люкс",
    "room_price": "14300",
    "room_volume": "2",
    "hotel": "1",
  },
]