import React from 'react';
import { Link } from 'react-router-dom';

import style from '../hotels.module.css'

export default function HotelCardComponent({ hotelsList }) {
  return(
    <div className={style.hotelCardList}>
      {hotelsList?.map((hotel) => (
        <HotelCardItemComponent key={hotel.id}
          hotelId={hotel.id}
          hotelName={hotel.title}
          hotelContacts={hotel.contacts}
          hotelAddress={hotel.address}
          roomsCount={hotel.rooms?.length}
          roomsVolumeTotal={hotel.hotel_rooms_volume}
        />
      ))}
    </div>
  );
}




function HotelCardItemComponent({ hotelId, hotelName, hotelAddress, hotelContacts, roomsCount, roomsVolumeTotal }) {
  return (
    <div className={style.hotelCardItem}>
      <Link className={style.hotelLink} to={`/hotels/${hotelId}`}>
        <div className={style.hotelCardMain}>
          <h4>{hotelName}</h4>
          <p>{hotelContacts}</p>
          <p>{hotelAddress}</p>
        </div>
      </Link>
      <div className={style.hotelCardContent}>
        <div className={style.contentData}>
          <h6>{roomsCount}</h6>
          <p>Количество номеров</p>
        </div>
        <div className={style.contentData}>
          <h6>{roomsVolumeTotal}</h6>
          <p>Вместимость номеров</p>
        </div>
      </div>
    </div>
  );
}