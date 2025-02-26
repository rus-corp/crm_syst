import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import style from '../styles/create_program.module.css'
import { NotificationComponent, CreateItemInput, SaveBtnComponent, ProfileInput, SmallButton } from '../../../../ui';
import ProgramEmployeeItemCreate from './ProgramEmployeeItemCreate';

import { getStaffs } from '../../../../api';

export default function ProgramExpenses() {
  const location = useLocation()
  const { programId, programTitle, nights } = location.state
  const [alert, setAlert] = React.useState({severity:'', message:''})
  const [staffExpenseItem, setStaffExpenseItem] = React.useState([{
    programID: programId,
    staffID: null,
    transfer: null,
    food: null,
    salary: null,
    habitation: null
  }])

  const [staffData, setStaffData] = React.useState([])
  const handleChangeExpense = (indx, name, value) => {
    setStaffExpenseItem(
      (prevData) => 
        prevData.map((item, ind) => 
        ind === indx ? {...item, [name]: value} : item)
    )
  }
  const handleChangeEmpl = (indx, value) => {
    setStaffExpenseItem(
      (prevData) => 
        prevData.map((item, ind) => 
        ind === indx ? {...item, staffID: value} : item)
    )
  }
  const handleSubmit = () => {
    console.log(staffExpenseItem)
  }

  const addComponent = () => {
    setStaffExpenseItem((prevData) => ([
      ...prevData,
      {
        programID: programId,
        staffID: '',
        transfer: '',
        food: '',
        salary: '',
        habitation: ''
      }
    ]))
  }
  const getStaffData = async () => {
    const response = await getStaffs()
    if (response.status === 200) {
      setStaffData(response.data)
    }
  }

  React.useEffect(() => {
    getStaffData()
  }, [])

  return(
    <section className={style.createProgram}>
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
            <h4>Затраты на сотрудников</h4>
          </div>
          <div className={style.orgExpense}>
            <div className={style.expenseItemHeader}>
              <p>Сотрудник</p>
              <p>Проезд</p>
              <p>Питание</p>
              <p>ЗП</p>
              <p>Проживание</p>
            </div>
            <div className={style.expenseStaff}>
              {staffExpenseItem.map((item, indx) => (
                <ProgramEmployeeItemCreate key={indx}
                staffData={staffData}
                indx={indx}
                handleChangeEmpl={handleChangeEmpl}
                handleChangeExpense={handleChangeExpense}
                />
              ))}
            </div>
            <SmallButton
            btnData={'Добавить сотрудника'}
            handleClick={addComponent}
            />
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