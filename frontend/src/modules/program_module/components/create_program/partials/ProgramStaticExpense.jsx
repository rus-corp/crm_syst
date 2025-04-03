import React from 'react';

import style from '../../styles/program_static_exp.module.css'
// import { CreateItemInput } from '@/ui'
import { CreateItemInput } from '../../../../../ui';


const staticCategoriesMap = {
  'organization': 'Затраты на организацию',
  'marketing': 'Реклама',
  'margin': 'Маржа',
  'merch': 'Мерчь'
}


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
          <span>{staticCategoriesMap[expenseTitle]}</span>
          <CreateItemInput
          value={expenseValue}
          changeFunc={handleChangeExpense}
          fieldType={'number'}
          />
        </div>
      </div>
    </div>
  );
}