import React from 'react';

import style from '../../styles/program_total.module.css'
import openList from '@/assets/app_img/open_btn.png'
import { ProfileInput } from '../../../../../ui';

export default function TotalStaticExpense({ staticExpenses }) {
  const totalExpense = staticExpenses?.reduce((acc, expense) => {
    return acc + expense.amount
  }
  , 0)
  const [activeList, setActiveList] = React.useState(false)
  return(
    <section className={style.staticExpenses}>
      <div className={style.expenseHeader}>
        <img className={`${activeList ? 'imgOpen' : ''}`} src={openList} alt="openList" onClick={() => setActiveList(!activeList)}/>
        <h5>Статические затраты программы</h5>
        <ProfileInput fieldData={totalExpense}/>
      </div>
      <div className={style.staticExpenseList}>
        {staticExpenses?.map((expenseItem) => (
          activeList && (
            <StaticExpenseItem key={expenseItem.id}
            itemCategory={expenseItem.category}
            expensePrice={expenseItem.amount}
            />
          )
        ))}
      </div>
    </section>
  );
}




function StaticExpenseItem ({ itemCategory, expensePrice }) {
  return (
    <div className={style.expenseItem}>
      <span>{staticCategoriesMap[itemCategory]}</span>
      <p>{expensePrice}</p>
    </div>
  );
}


const staticCategoriesMap = {
  'organization': 'Затраты на организацию',
  'marketing': 'Реклама',
  'margin': 'Маржа',
  'merch': 'Мерчь'
}