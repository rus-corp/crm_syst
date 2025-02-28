import React from 'react';

import style from '../../styles/hotelRooms.module.css'


import { getHotelByIdWithRooms } from '@/api';

export default function HotelRoomsList({ hotelId }) {
  const [hotelRooms, setHotelRooms] = React.useState([])
  const getHotelRoomsList = async (hotelId) => {
    const response = await getHotelByIdWithRooms(hotelId)
    if (response.status === 200) {
      console.log(response)
      setHotelRooms(response.data.rooms)
    }
  }
  React.useEffect(() => {
    getHotelRoomsList(hotelId)
  }, [hotelId])

  return(
    <div className={style.hotelRoomsList}>
      {hotelRooms.map((roomItem) => (
        <HotelRoomItem key={roomItem.id}
        roomType={roomItem.room_type}
        roomVolume={roomItem.room_volume}
        roomPrice={roomItem.room_price}
        />
      ))}
    </div>
  );
}


function HotelRoomItem({ roomType, roomVolume, roomPrice }) {
  return(
    <div className={style.roomItem}>
      <input type="checkbox" />
      <span>{roomType}</span>
      <span>{roomVolume}</span>
      <span>{roomPrice}</span>
    </div>
  );
}