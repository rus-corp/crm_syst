import React from 'react';

import style from './create_expense.module.css'
import { CreateNewItemBtn, ProfileInput } from '../../ui';


import { getExpensesList } from '../../api';


export default function ExpenseBlockComponent() {
  const [expenseData, setExpenseData] = React.useState([])

  const getExpenseData = async () => {
    const response = await getExpensesList()
    console.log(response.data)
    setExpenseData(response.data)
  }

  const handleChangeValue = (name, value) => {
    console.log(name, value)
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
        navi={'/create_item/create_expense'}
        />
      </div>
      <div className={style.blockContent}>
        {expenseData.map((expenseItem) => (
          <ExpenseItem key={expenseItem.id}
          expenseId={expenseItem.id}
          categoryTitle={expenseItem.category.title}
          amount={expenseItem.amount}
          />
        ))}
      </div>
    </div>
  );
}


function ExpenseItem({ amount, categoryTitle, expenseId}) {
  const [expenseData, setExpenseData] = React.useState({
    id: expenseId,
    expenseAmount: amount,
  })
  const handleChangeValue = (ev) => {
    const { name, value } = ev.target
    console.log(name, value)
    setExpenseData({
      ...expenseData,
      [name]: value
    })
  }
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleChangeExpense(expenseId, expenseData.expenseAmount)
    }
  }

  const handleChangeExpense = (expenseId, expenseAmount) => {
    console.log(expenseId, expenseAmount)
  }

  return (
    <div className={style.expenseItem}>
      <h5>{categoryTitle}</h5>
      <ProfileInput
      fieldName={'expenseAmount'}
      fieldType={'number'}
      fieldData={expenseData.expenseAmount}
      handleChange={handleChangeValue}
      handleKeyDown={handleKeyDown}
      />
    </div>
  );
}