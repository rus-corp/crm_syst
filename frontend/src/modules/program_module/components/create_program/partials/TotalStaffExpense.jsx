import React from 'react';

import style from '../../styles/program_total.module.css'
import openList from '@/assets/app_img/open_btn.png'
import { ProfileInput } from '../../../../../ui';
import { groupedStaffExpenses } from './utils';


export default function TotalStaffExpense({ staffExpenses }) {
  console.log(staffExpenses)
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
  console.log(Object.values(gropedData))
  return(
    <section className={style.staticExpenses}>
      <div className={style.expenseHeader}>
        <img className={`${activeList ? 'imgOpen' : ''}`} src={openList} alt="openList" onClick={() => setActiveList(!activeList)}/>
        <h5>Затраты на персонал</h5>
        <ProfileInput fieldData={totalExpense}/>
      </div>
      <div className={style.staticExpenseList}>
        {Object.values(gropedData).map((expenseItem) => (
          <StaffExpenseItem key={expenseItem.staffId}
          staffName={expenseItem.staffName}
          staffLastName={expenseItem.staffLastName}
          satffPosition={expenseItem.staffPosition}
          expenses={expenseItem.expenses}
          />
        ))}
      </div>
    </section>
  );
}


function StaffExpenseItem ({ staffName, staffLastName, satffPosition, expenses }) {
  return (
    <div className={style.expenseItem}>
      <div className={style.staffData}>
        <div className={style.staffName}>
          <p>Name</p>
          <h5>{staffName}</h5>
        </div>
        <div className={style.staffLastName}>
          <p>Last Name</p>
          <h5>{staffLastName}</h5>
        </div>
        <div className={style.staffPosition}>
          <p>Position</p>
          <h5>{satffPosition}</h5>
        </div>
      </div>
      <div className={style.staffItemExpenses}>

      </div>
      <p></p>
      <p>{satffPosition}</p>
      {expenses.map((expenseItem) => (
        <ExpenseItem key={expenseItem.id}
        itemCategory={expenseItem.category}
        expensePrice={expenseItem.price}
        />
      ))}
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