import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import style from '../styles/program_total.module.css'
import { NotificationComponent, ProfileInput, SaveBtnComponent } from '../../../../ui';
import TotalStaticExpense from './partials/TotalStaticExpense';
import TotalStaffExpense from './partials/TotalStaffExpense';

import { getProgramExpenses } from '../../../../api';

export default function TotalProgramComponent() {
  const location = useLocation()
  const navigation = useNavigate()
  const { programId, programTitle, nights } = location.state
  const handleSubmit = () => {}
  const [program, setProgram] = React.useState()
  const [staffExpense, setStaffExpense] = React.useState([])
  const [staticExpense, setStaticExpense] = React.useState([])
  const getProgramExpensesData = async (programData) => {
    const response = await getProgramExpenses(programData)
    if (response.status === 200) {
      console.log(response.data)
      setProgram(response.data)
      const staticExpense = response.data.expenses.filter((item) => item.employee_id === null)
      const staffExpense = response.data.expenses.filter((item) => item.employee_id !== null)
      setStaticExpense(staticExpense)
      setStaffExpense(staffExpense)
    }
  }
  React.useEffect(() => {
    getProgramExpensesData(programId)
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
            <h5>Программа с </h5>
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