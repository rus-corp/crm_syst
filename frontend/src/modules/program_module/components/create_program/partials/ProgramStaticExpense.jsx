import React from 'react';

import style from '../../styles/program_static_exp.module.css'
import { CreateItemInput } from '@/ui'


export default function ProgramStaticExpense() {
  return(
    <div className={style.saticExpenses}>
      <div className={style.fixedCosts}>
        <div className={style.costItem}>
          <span>Затраты на организацию</span>
          <CreateItemInput />
        </div>
        <div className={style.costItem}>
          <span>Реклама</span>
          <CreateItemInput />
        </div>
        <div className={style.costItem}>
          <span>Маржа</span>
          <CreateItemInput />
        </div>
        <div className={style.costItem}>
          <span>Мерчь</span>
          <CreateItemInput />
        </div>
      </div>
    </div>
  );
}