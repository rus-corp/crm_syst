import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import style from '../styles/create_program.module.css'
import { NotificationComponent, CreateItemInput, SaveBtnComponent, ProfileInput } from '../../../../ui';
import { StaffSelect } from '../../../../ui';

export default function ProgramExpenses() {
  const location = useLocation()
  const { programId, programTitle, nights } = location.state
  console.log(nights)
  const [alert, setAlert] = React.useState({severity:'', message:''})
  const [createProgramData, setCreateProgramData] = React.useState({
      title: '',
      start_date: '',
      end_date: '',
      place: '',
      desc: ''
    })
  
  const handleChange = (e) => {

  }
  const handleSubmit = () => {}

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

        <div className={style.sectionCreateData}>
          <aside className={style.orgExpense}>
            <div className={style.expenseItemHeader}>
              <p>Сотрудник</p>
              <p>Проезд</p>
              <p>Питание</p>
              <p>ЗП</p>
              <p>Проживание</p>
            </div>
            <div className={style.expenseStaff}>
              <div className={style.expenseItemHeader}>
                <StaffSelect />
                <CreateItemInput />
                <CreateItemInput />
                <CreateItemInput />
                <CreateItemInput />
              </div>
            </div>
            <button>Add Staff</button>
          </aside>
        </div>



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