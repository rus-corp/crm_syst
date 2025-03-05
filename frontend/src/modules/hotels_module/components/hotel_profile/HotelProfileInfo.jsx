import React from 'react';

import { ThreeComponentSwitch } from '@/ui';
import style from './styles/hotel_profile_info.module.css'
import HotelRoom from '../hotel_rooms/HotelRoom';

export default function HotelProfileInfo({ hotelRooms }) {
  return(
    <div className={style.hotelProfileInfoContainer}>
      <ThreeComponentSwitch />
      <div className={style.hotelRooms}>
        {hotelRooms?.map((room) => (
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
