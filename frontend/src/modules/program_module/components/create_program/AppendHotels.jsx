import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import style from '../styles/hotels_expenses.module.css'
import { NotificationComponent, CreateItemInput, SaveBtnComponent, ProfileInput } from '@/ui';
import ProgramHotelItem from './partials/ProgramHotelItem';
import { getHotelsWithoutRooms, appendHotelRoomToProgram } from '@/api';



export default function AppendHotels() {
  const navigation = useNavigate()
  const location = useLocation()
  const { programId, programTitle, nights } = location.state
  const [programRoom, setProgramRoom] = React.useState([])
  const [hotelList, setHotelList] = React.useState([])
  const [alert, setAlert] = React.useState({severity:'', message:''})
  
  const handleChange =() => {}
  
  const handleSubmit = () => {
    handleAppendRoomToProgramReq(programRoom)
  }

  const handleAppendRoomToProgramReq = async (hotelData) => {
    const response = await appendHotelRoomToProgram(hotelData)
    console.log(response)
    if (response.status === 201) {
      console.log('appended')
      setAlert({severity: 'success', message: 'Номера в программу добавлены'})
      setTimeout(() => {
        setAlert({severity:'', message:''})
        navigation(
          '/create_program/add_expenses', {
            state: {
              programId: programId,
              programTitle: programTitle,
              nights: nights
            }
          }
        )
      }, 2000);
    } else if (response.status !== 201) {
      setAlert({severity: 'error', message: response.data.detail})
    }
  }
  const handleAppendRoomToProgram = (hotel, room, state) => {
    if (state) {
      setProgramRoom((prevData) => (
        [
          ...prevData,
          {
            program_id: programId,
            hotel_id: hotel,
            room_id: room
          }
        ]
      ))
    } else if (!state) {
      setProgramRoom((prevData) => (
        prevData.filter((roomItem) => roomItem.room_id !== room)
      ))
    }
  }

  const getHotelsList = async () => {
    const response = await getHotelsWithoutRooms()
    if (response.status === 200) {
      setHotelList(response.data)
    }
  }

  React.useEffect(() => {
    getHotelsList()
  }, [])

  return(
    <section className={style.createDataProgram}>
      <div className={style.createProgramData}>
        <div className={style.sectionHeader}>
          <h2>Добавить Проживание для {programTitle}</h2>
          <NotificationComponent
          severity={alert.severity}
          message={alert.message}
          />
        </div>
        <div className={style.expenseHeader}>
          <div className={style.programStaticData}>
            <ProfileInput
            fieldData={nights}
            fieldTitle='Количество ночей'
            />
          </div>
          <div className={style.programStaticData}>
            <ProfileInput
            fieldData='15'
            fieldTitle='Количество человек'
            />
          </div>
        </div>




        <aside className={style.sectionCreateData}>
          <div className={style.dataHeader}>
            <h4>Добавить проживание</h4>
          </div>
          <div className={style.sectionAppendHotels}>
            <div className={style.hotelList}>
              {hotelList.map((hotelItem) => (
                <ProgramHotelItem key={hotelItem.id}
                hotelId={hotelItem.id}
                hotelTitle={hotelItem.title}
                hotelCity={hotelItem.city}
                hotelAddress={hotelItem.address}
                handleAppendRoomToProgram={handleAppendRoomToProgram}
                />
              ))}
            </div>
          </div>
        </aside>





        <div className={style.saveBtn}>
          <SaveBtnComponent
          saveTitle='Программу'
          clicked={handleSubmit}
          />
        </div>
      </div>
    </section>
  );
}