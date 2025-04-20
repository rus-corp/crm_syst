import React from 'react';

import style from '../../styles/program_total.module.css'
import openList from '@/assets/app_img/open_btn.png'
import { ProfileInput } from '../../../../../ui';
import { groupedStaffExpenses } from './utils';


export default function TotalStaffExpense({ staffExpenses }) {
  const [activeList, setActiveList] = React.useState(false)
  const totalExpense = staffExpenses?.reduce((acc, expense) => {
    return acc + expense.amount
  }, 0)
  const gropedData = React.useMemo(() => {
    return groupedStaffExpenses(staffExpenses)
  }, [staffExpenses])
  // const handleMakeData = () => {
  //   const groupedData = groupedStaffExpenses(staffExpenses)
  //   setStaffData(Object.values(groupedData))
  // }
  // const handleClick = () => {
  //   handleMakeData()
  //   setActiveList(!activeList)
  //   console.log(staffData)
  // }
  return(
    <section className={style.staticExpenses}>
      <div className={style.expenseHeader}>
        <img className={`${activeList ? 'imgOpen' : ''}`} src={openList} alt="openList" onClick={() => setActiveList(!activeList)}/>
        <h5>Затраты на персонал</h5>
        <ProfileInput fieldData={totalExpense}/>
      </div>
      <div className={style.staticExpenseList}>
        {Object.values(gropedData).map((expenseItem) => (
          activeList && (
            <StaffExpenseItem key={expenseItem.staffId}
            staffName={expenseItem.staffName}
            staffLastName={expenseItem.staffLastName}
            satffPosition={expenseItem.staffPosition}
            expenses={expenseItem.expenses}
            />
          )
        ))}
      </div>
    </section>
  );
}


function StaffExpenseItem ({ staffName, staffLastName, satffPosition, expenses }) {
  return (
    <div className={style.expenseItem}>
      <div className={style.staffData}>
        <div className={style.staffDataContent}>
          <p>Имя</p>
          <p>Фамилия</p>
          <p>Должность</p>
        </div>
        <div className={style.staffDataContent}>
          <span>{staffName}</span>
          <span>{staffLastName}</span>
          <span>{satffPosition}</span>
        </div>
      </div>
      <div className={style.staffExpenseList}>
        {expenses.map((expenseItem) => (
          <ExpenseItem key={expenseItem.id}
          itemCategory={expenseItem.category}
          expensePrice={expenseItem.price}
          />
        ))}

      </div>
    </div>
  );
}




function ExpenseItem({ itemCategory, expensePrice }) {
  return (
    <div className={style.expenseItem}>
      <p>{categoryMap[itemCategory]}</p>
      <p>{expensePrice}</p>
    </div>
  );
}

const categoryMap = {
  'transfer': 'Проезд',
  'food': 'Питание',
  'salary': 'ЗП',
  'habitation': 'Проживание'
}