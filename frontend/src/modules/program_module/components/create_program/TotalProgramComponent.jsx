import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import style from '../styles/program_total.module.css'
import { NotificationComponent, ProfileInput, SaveBtnComponent } from '../../../../ui';
import TotalStaticExpense from './partials/TotalStaticExpense';
import TotalStaffExpense from './partials/TotalStaffExpense';
import TotalProgramPrice from './partials/TotalProgramPrice';
import TotalProgramPartner from './partials/TotalProgramPartner';

import {
  getProgramExpenses,
  getProgramHotelRooms,
  getProgramPartners,
  getProgramPrices
} from '../../../../api';


export default function TotalProgramComponent() {
  const location = useLocation()
  const navigation = useNavigate()
  const { programId, programTitle, nights } = location.state
  const handleSubmit = () => {
    setAlert({severity: 'success', message: 'Программа успешно сохранена'})
    setTimeout(() => {
      setAlert({severity: '', message: ''})
      navigation('/programs')
    }, 2000)
  }
  const [program, setProgram] = React.useState()
  const [staffExpense, setStaffExpense] = React.useState([])
  const [staticExpense, setStaticExpense] = React.useState([])
  const [hotelRooms, setHotelRooms] = React.useState([])
  const [partners, setPartners] = React.useState([])
  const [programPrices, setProgramPrices] = React.useState({})
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const getProgramExpensesData = async (programData) => {
    const response = await getProgramExpenses(programData)
    if (response.status === 200) {
      setProgram(response.data)
      const staticExpense = response.data.expenses.filter((item) => item.employee_id === null)
      const staffExpense = response.data.expenses.filter((item) => item.employee_id !== null)
      setStaticExpense(staticExpense)
      setStaffExpense(staffExpense)
    }
  }
  const getHotelRooms = async (programData) => {
      const response = await getProgramHotelRooms(programData)
      if (response.status === 200) {
        const hotels = response.data
        const allRooms = hotels.flatMap((hotel) => hotel.rooms)
        setHotelRooms(allRooms)
      }
    }
  const handleProgramPartners = async (programData) => {
    const response = await getProgramPartners(programData)
    if (response.status === 200) {
      setPartners(response.data)
    }
  }
  const handleGetProgramPrices = async (programData) => {
    const response = await getProgramPrices(programData)
    if (response.status === 200) {
      setProgramPrices(response.data.prices)
    }
  }
  React.useEffect(() => {
    getProgramExpensesData(programId)
    getHotelRooms(programId)
    handleProgramPartners(programId)
    handleGetProgramPrices(programId)
  }, [])
  return(
    <section className={style.createProgram}>
      <div className={style.createProgramData}>
        <div className={style.sectionHeader}>
          <h2>Итоговая стоимость {programTitle}</h2>
          <NotificationComponent
          severity={alert.severity}
          message={alert.message}
          />
        </div>
        <div className={style.programData}>
          <div className={style.programDataHeader}>
            <h5>Даты программы</h5>
            <ProfileInput
            fieldData={program?.start_date}
            />
            <ProfileInput
            fieldData={program?.end_date}
            />
          </div>
          <div className={style.programStaticData}>
          </div>
        </div>
        <aside className={style.sectionCreateData}>
          <div className={style.dataHeader}>
            <h4>Затраты</h4>
          </div>
          <div className={style.staticExpense}>
            <TotalStaticExpense
            staticExpenses={staticExpense}
            />
          </div>
          <div className={style.staffExpense}>
            <TotalStaffExpense
            staffExpenses={staffExpense}
            />
          </div>
          <div className={style.staffExpense}>
            <TotalProgramPartner
            partnerData={partners}
            />
          </div>
          <TotalProgramPrice
          programPrices={programPrices}
          hotelRooms={hotelRooms}
          />
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