import React from 'react';
import { useLocation } from 'react-router-dom';

import style from './create_hotel.module.css'
import { CreateItemInput, SaveBtnComponent, TextAreaComponent } from '../../../../ui';


export default function CreateRoom() {
  const location = useLocation()
  const { hotelId, hotelTitle } = location.state
  const [roomData, setRoomData] = React.useState({
    room_type: '',
    room_price: 0,
    room_volume: 0,
    hotel_id: hotelId
    })

  const handleChangeField = (name, value) => {
    setRoomData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleSubmit = () => {
    console.log(roomData)
  }

  return(
    <section className={style.createHotel}>
          <div className={style.createHotelData}>
            <div className={style.sectionHeader}>
              <h3>Добавить номера отеля {hotelTitle}</h3>
            </div>
            <div className={style.sectionCreateData}>
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
              <div className={style.saveBtn}>
                <SaveBtnComponent
                saveTitle='Номера'
                clicked={handleSubmit}
                />
              </div>
            </div>
          </div>
        </section>
  );
}