import React from 'react';
import { useLocation } from 'react-router-dom';

import style from '../styles/hotels_expenses.module.css'
import { NotificationComponent, CreateItemInput, SaveBtnComponent, ProfileInput } from '@/ui';
import ProgramHotelItem from './partials/ProgramHotelItem';
import { getHotelsWithoutRooms } from '@/api';



export default function AppendHotels() {
  const location = useLocation()
  const { programId, programTitle, nights } = location.state
  const [showList, setShowList] = React.useState(false)
  const [createProgramData, setCreateProgramData] = React.useState({
    title: '',
    start_date: '',
    end_date: '',
    place: '',
    desc: ''
  })
  const [hotelList, setHotelList] = React.useState([])
  const [alert, setAlert] = React.useState({severity:'', message:''})
  const handleChange =() => {}
  const handleSubmit = () => {}
  const handleShowList = () => setShowList(!showList)

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
          <h2>Затраты на программу {programTitle}</h2>
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