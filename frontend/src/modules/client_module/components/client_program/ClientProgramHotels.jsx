import React from 'react';

import style from './styles/program_hotels.module.css'
import { SmallButton, CheckInModal } from '../../../../ui';
import openList from '@/assets/app_img/open_btn.png'

import { getProgramHotelRooms, getProgramRoomClient } from '../../../../api';


export default function ClientProgramHotels({ programId }) {
  const [programHotels, setProgramHotels] = React.useState([])
  const handleProgramRooms = async (programData) => {
    const response = await getProgramHotelRooms(programData)
    if (response.status === 200) {
      console.log(response.data)
      setProgramHotels(response.data)
    }
  }

  React.useEffect(() => {
    handleProgramRooms(programId)
  }, [])
  return(
    <section className={style.currentClientProgram}>
      <div className={style.clientProgramInfo}>
        <div className={style.programInfoTitle}>
          <h5>Текущее проживание</h5>
        </div>
      </div>
      <div className={style.programHotelDesc}>
        {programHotels.map((hotelItem) => (
          <HotelItem key={hotelItem.id}
          hotelTitle={hotelItem.title}
          hotelContacts={hotelItem.contacts}
          hotelAddress={hotelItem.address}
          hotelRooms={hotelItem.rooms}
          hotelRoomVol={hotelItem.hotel_rooms_volume}
          programRoomId={hotelItem.program_room_id}
          />
        ))}
      </div>
    </section>
  );
}




function HotelItem({
  hotelTitle,
  hotelContacts,
  hotelAddress,
  hotelRooms,
  hotelRoomVol,
  programRoomId
}) {
  const [activeList, setActiveList] = React.useState(false)

  const handleClickImg = () => setActiveList(!activeList)
  return (
    <div className={style.hotelItem}>
      <div className={style.hotelContent}>
        <div className={style.hotelMainData}>
          <div className={style.dataItem}>
            <p>Название отеля</p>
            <h6>{hotelTitle}</h6>
          </div>
          <div className={style.dataItem}>
            <p>Телефон</p>
            <h6>{hotelContacts}</h6>
          </div>
        </div>
        <div className={style.hotelAddress}>
          <div className={style.dataItem}>
            <p>Адресс</p>
            <h6>{hotelAddress}</h6>
          </div>
          <div className={style.dataItem}>
            <p>Вместимость номеров</p>
            <h6>{hotelRoomVol}</h6>
          </div>
        </div>
      </div>
      <div className={style.hotelRooms}>
        <div className={style.roomsHeader}>
          <h6>Номера отеля</h6>
          <img className={`${activeList ? 'imgOpen' : ''}`} src={openList} alt="openList" onClick={handleClickImg}/>
        </div>
        <div className={style.roomsList}>
          {activeList && (
            hotelRooms.map((roomItem) => (
              <RoomItem key={roomItem.id}
              roomVol={roomItem.room_volume}
              roomType={roomItem.room_type}
              roomPrice={roomItem.room_price}
              programRoomId={programRoomId}
              />
            ))
          )}
        </div>
      </div>
    </div>
  );
}



function RoomItem({ roomVol, roomType, roomPrice, programRoomId }) {
  const [open, setOpen] = React.useState(false)
  const handleClick = () => setOpen(true)
  const handleGetRoomClient = async () => {}
  return (
    <div className={style.roomItem}>
      <div className={style.roomDataItem}>
        <p>Тип номера</p>
        <h6>{roomType}</h6>
      </div>
      <div className={style.roomDataItem}>
        <p>Вместимость номера</p>
        <h6>{roomVol}</h6>
      </div>
      <div className={style.roomDataItem}>
        <p>Цена номера</p>
        <h6>{roomPrice}</h6>
      </div>
      <SmallButton
      btnData={'Заселить'}
      handleClick={handleClick}
      />
      <CheckInModal
      visible={open}
      close={() => setOpen(false)}
      programRoomId={programRoomId}
      />
    </div>
  );
}