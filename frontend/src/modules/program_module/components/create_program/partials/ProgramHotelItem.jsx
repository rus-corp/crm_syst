import React from 'react';

import style from '../../styles/program_hotels.module.css'
import openList from '../../../../../assets/app_img/open_btn.png'

import HotelRoomsList from './HotelRoomsList';


export default function ProgramHotelItem({
  hotelId,
  hotelTitle,
  hotelCity,
  hotelAddress,
  handleAppendRoomToProgram
}) {
  const [activeList, setActiveList] = React.useState(false)
  const handleClick = () => setActiveList(!activeList)
  const [hotelRooms, setHotelRooms] = React.useState([])
  const handleAppendHotelRooomToProgram = (roomId, state) => {
    handleAppendRoomToProgram(hotelId, roomId, state)
  }
  
  return(
    <>
      <div className={style.hotelData} onClick={handleClick}>
        <div className={style.itemImg}>
          <img className={`${activeList ? 'imgOpen' : ''}`} src={openList} alt="openList" />
        </div>
        <div className={style.hotelTitle}>
          <h5>{hotelTitle}</h5>
        </div>
        <div className={style.hotelAddress}>
          <span>{hotelAddress}</span>
        </div>
        <div className={style.hotelCity}>
          <p>{hotelCity}</p>
        </div>
      </div>
      {activeList && 
        <HotelRoomsList
        hotelId={hotelId}
        handleAppendRoomToProgram={handleAppendHotelRooomToProgram}
        />
      }
    </>
  );
}