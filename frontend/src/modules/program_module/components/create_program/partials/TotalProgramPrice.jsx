import React from 'react';

import style from '../../styles/program_total.module.css'
import { CreateItemInput } from '../../../../../ui';


export default function TotalProgramPrice({ programPrices, hotelRooms }) {

  return(
    <div className={style.programTotalPrice}>
      <div className={style.blockHeader}>
        <h4>Стоимость поездки</h4>
      </div>
      <div className={style.totalPriceData}>
        <CreateItemInput fieldTitle={'Базовая цена'} value={programPrices.base_price}/>
        <CreateItemInput fieldTitle={'Не первый раз'} value={programPrices.loayal_price}/>
        <CreateItemInput fieldTitle={'Комюнити'} value={programPrices.comunity_price}/>
      </div>
      <div className={style.roomsList}>
        {hotelRooms.map((roomItem) => (
          <RoomItem key={roomItem.id}
          roomName={roomItem.room_type}
          roomVolume={roomItem.room_volume}
          roomPrice={roomItem.room_price}
          programPrices={programPrices}
          />
        ))}
      </div>
    </div>
  );
}


function RoomItem({ roomName, roomPrice, roomVolume, programPrices }) {
  return (
    <div className={style.roomItem}>
      <div className={style.roomItemData}>
        <div className={style.dataItem}>
          <p>Название номера</p>
          <span>{roomName}</span>
        </div>
        <div className={style.dataItem}>
          <p>Вместимость</p>
          <span>{roomVolume}</span>
        </div>
        <div className={style.dataItem}>
          <p>Стоимость номера</p>
          <span>{roomPrice}</span>
        </div>
      </div>
      <div className={style.roomTotal}>
        <div className={style.blockHeader}>
          <p>Итого стоимость поездки</p>
        </div>
        <div className={style.prices}>
          <CreateItemInput
          fieldWidth={'50%'}
          value={programPrices.base_price + roomPrice}
          fieldTitle={'В первый раз'}
          />
          <CreateItemInput
          fieldWidth={'50%'}
          value={programPrices.loayal_price + roomPrice}
          fieldTitle={'Не первый раз'}
          />
          <CreateItemInput
          fieldWidth={'50%'}
          value={programPrices.comunity_price + roomPrice}
          fieldTitle={'Цена комьюнити'}
          />
        </div>
      </div>
    </div>
  );
}