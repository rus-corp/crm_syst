import React from 'react';

import style from './hotel_room.module.css'

export default function HotelRoom({ roomType, roomPrice, roomVolume}) {
  return(
    <div className={style.hoteRoomItem}>
      <div className={style.roomData}>
        <h6>{roomType}</h6>
        <div className={style.roomDataDesc}>
          <p>Вместимость: {roomVolume}</p>
          <p>Цена: {roomPrice}</p>
        </div>
      </div>
      <div className={style.roomGuests}>
        <h6>Проживающие</h6>
        <div className={style.roomGuestsData}>
          <div className={style.placeData}>
            <p>Количество мест</p>
            <h6>2</h6>
          </div>
          <div className={style.placeData}>
            <p>Свободных мест</p>
            <h6>1</h6>
          </div>
          <div className={style.placeData}>
            <p>Занятых мест</p>
            <h6>1</h6>
          </div>
        </div>
      </div>
    </div>
  );
}