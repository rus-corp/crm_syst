import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import style from './create_hotel.module.css'
import { SaveBtnComponent } from '../../../../ui';
import CreateRoomItem from './CreateRoomItem';
import { SmallButton } from '../../../../ui';
import { createRoomsList } from '../../../../api';
import { cleanData } from '../../utils/utils';


export default function CreateRoom() {
  const navigation = useNavigate()
  const location = useLocation()
  const { hotelId, hotelTitle } = location.state
  const [roomData, setRoomData] = React.useState([{
    room_type: '',
    room_price: 0,
    room_volume: 0,
    hotel_id: hotelId
    }])
  
  const createRoomsDataList = async (roomsListData) => {
    const cleanRooms = cleanData(roomsListData)
    const response = await createRoomsList(cleanRooms)
    console.log(response)
    if (response.status === 201) {
      navigation('/hotels')
    }
    return response
  }
  
  const addComponent = () => {
    setRoomData((prevData) => [
      ...prevData,
      {room_type: '',
      room_price: 0,
      room_volume: 0,
      hotel_id: hotelId}
    ])
  }

  const handleChangeField = (index, name, value) => {
    setRoomData(
      (prevData) => 
        prevData.map((item, ind) => 
        ind === index ? {...item, [name]: value} : item)
    )
  }

  const handleSubmit = () => {
    createRoomsDataList(roomData)
  }

  return(
    <section className={style.createHotel}>
          <div className={style.createHotelData}>
            <div className={style.sectionHeader}>
              <h3>Добавить номера отеля {hotelTitle}</h3>
            </div>
            <div className={style.sectionCreateData}>
              {roomData.map((data, index) => (
                <CreateRoomItem key={index}
                index={index}
                roomData={data}
                handleChange={handleChangeField}/>
              ))}
              <SmallButton
              btnData='добавить номер'
              handleClick={addComponent}
              />
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