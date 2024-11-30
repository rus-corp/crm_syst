import React from 'react';

import style from './styles/hotelsList.module.css'

import { getProgramHotels } from '../../../api';




export default function HotelsListComponent({ programId }) {
  const [programHotels, setProgramHotels] = React.useState([])

  const handleGetProgramHotels = async(id) => {
    const response = await getProgramHotels(id)
    if (response.status === 200) {
      setProgramHotels(response.data)
    }
  }

  React.useEffect(() => {
    if (programId) {
      handleGetProgramHotels(programId)
    }
  }, [programId])
  return(
    <>
      <div className={style.activeHotels}>
        <div className={style.activeHotelsHeader}>
          <h4>Проживание Программы</h4>
        </div>
        <div className={style.hotelsList}>
          {programHotels.map((hotelItem) => (
            <HotelItem key={hotelItem.id}
            hotelTitle={hotelItem.title}
            roomsCount={hotelItem.rooms.length}
            roomVolume={hotelItem.hotel_rooms_volume}
            />
          ))}
        </div>
      </div>
    </>
  );
}


function HotelItem({ hotelTitle, roomsCount, roomVolume }) {
  return (
    <div className={style.hotelItem}>
      <div className={style.hotelItemData}>
        <p>Название</p>
        <h5>{hotelTitle}</h5>
      </div>
      <div className={style.hotelItemData}>
        <p>Номера</p>
        <div className={style.hotelItemData__volumes}>
          <div className={style.numberInfo}>
            <p>Занято</p>
            <h6>{roomsCount}</h6>
          </div>
          <div className={style.numberInfo}>
            <p>Свободно</p>
            <h6>2</h6>
          </div>
        </div>
      </div>
      <div className={style.hotelItemData}>
        <p>Места</p>
        <div className={style.hotelItemData__volumes}>
          <div className={style.numberInfo}>
            <p>Занято</p>
            <h6>{roomVolume}</h6>
          </div>
          <div className={style.numberInfo}>
            <p>Свободно</p>
            <h6>2</h6>
          </div>
        </div>
        
      </div>
    </div>
  );
}
