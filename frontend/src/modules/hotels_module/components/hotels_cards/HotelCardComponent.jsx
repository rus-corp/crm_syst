import React from 'react';
import { Link } from 'react-router-dom';

import style from '../hotels.module.css'

export default function HotelCardComponent({ hotelsList }) {
  return(
    <div className={style.hotelCardList}>
      {hotelsList?.map(hotel => 
        <div className={style.hotelCardItem} key={hotel.id}>
          <HotelCardItemComponent key={hotel.id}
          hotelId={hotel.id}
          hotelName={hotel.name}
          hotelContacts={hotel.contacts}
          hotelAddress={hotel.address}
          roomsCount={12}
          freeRooms={4}
          unFreeRooms={5}
          />
        </div>
      )}
    </div>
  );
}




function HotelCardItemComponent({ hotelId, hotelName, hotelAddress, hotelContacts, roomsCount, freeRooms, unFreeRooms }) {
  return (
    <>
      <div className={style.hotelCardMain}>
        <Link className={style.hotelLink} to={`/hotels/${hotelId}`}><h4>{hotelName}</h4></Link>
        <p>{hotelContacts}</p>
        <p>{hotelAddress}</p>
      </div>
      <div className={style.hotelCardContent}>
        <div className={style.contentData}>
          <h6>{roomsCount}</h6>
          <p>Количество номеров</p>
        </div>
        <div className={style.contentData}>
          <h6>{freeRooms}</h6>
          <p>Свободных номеров</p>
        </div>
        <div className={style.contentData}>
          <h6>{unFreeRooms}</h6>
          <p>Занятых номеров</p>
        </div>
      </div>
    </>
  );
}