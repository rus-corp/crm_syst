import React from 'react';
import { Link } from 'react-router-dom';

import style from '../styles/company_main.module.css'
import { getExpensesList } from '../../../api';


export default function ExpenseBlock() {
  const [expenses, setExpenses] = React.useState([])
  const getExpenseData = async () => {
    const response = await getExpensesList(true)
    setExpenses(response.data)
  }
  React.useEffect(() => {
    getExpenseData()
  }, [])
  return(
    <div className={style.staffBlock} style={{marginTop: '-1rem'}}>
      <div className={style.staffTitle}>
        <h4>Затраты</h4>
        <Link to='/company/expenses'>Показать все &gt;</Link>
      </div>
      <div className={style.staffList}>
        {expenses.map((staffItem) => (
          <ExpenseItem key={staffItem.id}
          categoryTitle={staffItem.category.title}
          amount={staffItem.amount}
          />
        ))}
      </div>
    </div>
  );
}



function ExpenseItem({ categoryTitle, amount}) {
  return (
    <div className={style.expenseItem}>
      <span>{categoryTitle}</span>
      <span>{amount}</span>
    </div>
  );
}



