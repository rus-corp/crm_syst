import React from 'react';

import style from './create_hotel.module.css'
import { CreateItemInput } from '../../../../ui';


export default function CreateRoomItem({ index, roomData, handleChange }) {

  const handleChangeField = (name, value) => {
    handleChange(index, name, value)
  }

  return(
    <div className={style.flexRoomsFields}>
      <div className={style.createdField}>
        <CreateItemInput
        fieldTitle='Тип Номера'
        fieldType='text'
        fieldName='room_type'
        value={roomData.room_type}
        changeFunc={handleChangeField}
        />
      </div>
      <div className={style.createdField}>
        <CreateItemInput
        fieldTitle='Вместимость номера'
        fieldType='number'
        fieldName='room_volume'
        value={roomData.room_volume}
        changeFunc={handleChangeField}
        />
      </div>
      <div className={style.createdField}>
        <CreateItemInput
        fieldTitle='Цена'
        fieldType='number'
        fieldName='room_price'
        value={roomData.room_price}
        changeFunc={handleChangeField}
        />
      </div>
    </div>
  );
}