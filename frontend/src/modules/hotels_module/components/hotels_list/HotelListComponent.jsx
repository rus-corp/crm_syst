import React from 'react';
import { Link } from 'react-router-dom';

import itemBurger from '@/assets/menu_icons/item_burger.svg'
import style from '../hotels.module.css'


export default function HotelListComponent({ hotelsList}) {
  
  return(
    <>
      {hotelsList?.map(hotel => 
        <div className={style.hotelListItem} key={hotel.id}>
          <HotelComponent key={hotel.id}
          hotelId={hotel.id}
          hotelName={hotel.title}
          hotelContacts={hotel.contacts}
          hotelCity={hotel.city}
          hotelAddress={hotel.address}
          />
        </div>
      )}
    </>
  );
}





function HotelComponent({ hotelId, hotelName, hotelContacts, hotelCity, hotelAddress }) {
  return (
    <>
      <div className={style.hotelData}>
        <Link to={`/hotels/${hotelId}`}><h4>{hotelName}</h4></Link>
        <p>{hotelContacts}</p>
      </div>
      <div className={style.hotelData}>
        <p>Город</p>
        <h6>{hotelCity}</h6>
      </div>
      <div className={style.hotelData}>
        <p>Адресс</p>
        <h6>{hotelAddress}</h6>
      </div>
      <div className={style.itemMenu}>
        <img src={itemBurger} alt="burger" />
      </div>
    </>
  )
}