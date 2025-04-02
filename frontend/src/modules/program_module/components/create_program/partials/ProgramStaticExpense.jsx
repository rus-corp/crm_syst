import React from 'react';

import style from '../../styles/program_static_exp.module.css'
// import { CreateItemInput } from '@/ui'
import { CreateItemInput } from '../../../../../ui';


export default function ProgramStaticExpense({
  indx,
  expenseTitle,
  expenseValue,
  handleChange
}) {
  const handleChangeExpense = (name, value) => {
    handleChange(indx, name, value)
  }
  return(
    <div className={style.saticExpenses}>
      <div className={style.fixedCosts}>
        <div className={style.costItem}>
          <span>{expenseTitle}</span>
          <CreateItemInput
          fieldName={'organiztion'}
          value={expenseValue}
          changeFunc={handleChangeExpense}
          fieldType={'number'}
          />
        </div>
        {/* <div className={style.costItem}>
          <span>Реклама</span>
          <CreateItemInput
          fieldName={'marketing'}
          // value={marketingExpense}
          changeFunc={handleChangeExpense}
          fieldType={'number'}
          />
        </div>
        <div className={style.costItem}>
          <span>Маржа</span>
          <CreateItemInput
          fieldName={'margin'}
          // value={marginExpense}
          changeFunc={handleChangeExpense}
          fieldType={'number'}
          />
        </div>
        <div className={style.costItem}>
          <span>Мерчь</span>
          <CreateItemInput
          changeFunc={handleChangeExpense}
          />
        </div> */}
      </div>
    </div>
  );
}