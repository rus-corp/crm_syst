import React from 'react';

import style from './create_expense.module.css'
import { CreateNewItemBtn } from '../../ui';

import { getExpensesList } from '../../api';

export default function CreateExpense() {
  const [expenseData, setExpenseData] = React.useState([])

  const getExpenseData = async () => {
    const response = await getExpensesList()
    setExpenseData(response.data)
  }

  React.useEffect(() => {
    getExpenseData()
  }, [])

  return(
    <div className={style.createBlock}>
      <div className={style.blockHeader}>
        <h2>Затраты</h2>
        <CreateNewItemBtn
        createDataName='Затрату'
        />
      </div>
      <div className={style.blockContent}>
        {expenseData.map((staffItem) => (
          <ExpenseItem
          />
        ))}
      </div>
    </div>
  );
}


function ExpenseItem() {
  return (
    <p></p>
  );
}