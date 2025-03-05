import React from 'react';

import style from '../../styles/hotelRooms.module.css'


import { getHotelByIdWithRooms } from '@/api';

export default function HotelRoomsList({ hotelId, handleAppendRoomToProgram }) {
  const [hotelRooms, setHotelRooms] = React.useState([])
  const getHotelRoomsList = async (hotelId) => {
    const response = await getHotelByIdWithRooms(hotelId)
    if (response.status === 200) {
      setHotelRooms(response.data.rooms)
    }
  }
  React.useEffect(() => {
    getHotelRoomsList(hotelId)
  }, [hotelId])

  return(
    <div className={style.hotelRoomsList}>
      <div className={style.hotelRoomHeader}>
        <p></p>
        <p>Описание</p>
        <p>Вместимость</p>
        <p>Стоимость</p>
      </div>
      {hotelRooms.map((roomItem) => (
        <HotelRoomItem key={roomItem.id}
        roomId={roomItem.id}
        roomType={roomItem.room_type}
        roomVolume={roomItem.room_volume}
        roomPrice={roomItem.room_price}
        handleAppendRoom={handleAppendRoomToProgram}
        />
      ))}
    </div>
  );
}


function HotelRoomItem({ roomId, roomType, roomVolume, roomPrice, handleAppendRoom }) {
  const [isSelected, setIsSelected] = React.useState(false)
  const appendRoomToProgram = () => {
    const newState = !isSelected
    setIsSelected(newState)
    handleAppendRoom(roomId, newState)
  }
  return(
    <div className={style.roomItem}>
      <input type="checkbox" checked={isSelected} onChange={() => appendRoomToProgram()}/>
      <span>{roomType}</span>
      <span>{roomVolume}</span>
      <span>{roomPrice}</span>
    </div>
  );
}