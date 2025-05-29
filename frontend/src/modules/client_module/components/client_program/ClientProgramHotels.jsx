import React from 'react';

import style from './styles/program_hotels.module.css'
import { SmallButton, CheckInModal, CheckOutModal } from '../../../../ui';
import { useSelector } from 'react-redux';


import openList from '@/assets/app_img/open_btn.png'

import { getProgramHotelRooms, getProgramRoomClient } from '../../../../api';


export default function ClientProgramHotels({ programId }) {
  const [programHotels, setProgramHotels] = React.useState([])
  const handleProgramRooms = async (programData) => {
    const response = await getProgramHotelRooms(programData)
    if (response.status === 200) {
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
  hotelRoomVol
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
              programRoomId={roomItem.program_room_id}
              />
            ))
          )}
        </div>
      </div>
    </div>
  );
}



function RoomItem({ roomVol, roomType, roomPrice, programRoomId }) {
  const slug = useSelector((state) => state.client.clientSlug)
  const [roomClient, setRoomClient] = React.useState([])
  const [clientInRoom, setClientInRoom] = React.useState(false)
  const handleGetRoomClient = async (programRoomData) => {
    const response = await getProgramRoomClient(programRoomData)
    if (response.status === 200) {
      const responseData = response.data
      const roomClientsLastName = responseData.map((item) => `${item.program_clients.client.last_name} ${item.program_clients.client.name}`)
      setRoomClient(roomClientsLastName)
      const clientHasInRoom = responseData.find((item) => item.program_clients.client.slug === slug)
      setClientInRoom(!!clientHasInRoom)
      handleBtnLabel(!!clientHasInRoom)
    }
  }
  const [btnLabel, setBtnLabel] = React.useState('')
  const [Inopen, setInOpen] = React.useState(false)
  const [outOpen, setOutOpen] = React.useState(false)

  const handleClick = () => {
    if (btnLabel === 'Заселить') {
      setInOpen(true)
    } else if (btnLabel === 'Выселить') {
      setOutOpen(true)
    }
    
  }

  const handleBtnLabel = (clientInRoom) => {
    if (clientInRoom) {
      setBtnLabel('Выселить')
    }else {
      setBtnLabel('Заселить')
    }
  }

  React.useEffect(() => {
    handleGetRoomClient(programRoomId)
  }, [programRoomId])
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
      <div className={style.roomClient}>
        {roomClient?.map((client, indx) => (
          <p key={indx}>{client}</p>
        ))}
          <SmallButton
            btnData={btnLabel}
            handleClick={handleClick}
            />
      </div>
      <CheckInModal
      visible={Inopen}
      close={() => setInOpen(false)}
      programRoomId={programRoomId}
      // dataFunc={clientInRoom}
      />
      <CheckOutModal
      visible={outOpen}
      close={() => setOutOpen(false)}
      programRoomId={programRoomId}
      />
    </div>
  );
}