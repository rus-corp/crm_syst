import React from 'react';

import style from '../../styles/create_program.module.css'
import { SmallButton } from '@/ui';
import ProgramEmployeeItemCreate from './ProgramEmployeeItemCreate';

export default function StaffExpensePart({
  staffExpenseItem,
  staffData,
  handleChangeEmpl,
  handleChangeExpense, 
  addComponent
}) {

  return(
    <aside className={style.sectionCreateData}>
      <div className={style.dataHeader}>
        <h4>Затраты на сотрудников</h4>
      </div>
      <div className={style.orgExpense}>
        <div className={style.expenseItemHeader}>
          <p>Сотрудник</p>
          <p>Проезд</p>
          <p>Питание</p>
          <p>ЗП</p>
          <p>Проживание</p>
        </div>
        <div className={style.expenseStaff}>
          {staffExpenseItem.map((item, indx) => (
            <ProgramEmployeeItemCreate key={indx}
            staffData={staffData}
            indx={indx}
            handleChangeEmpl={handleChangeEmpl}
            handleChangeExpense={handleChangeExpense}
            />
          ))}
        </div>
        <SmallButton
        btnData={'Добавить сотрудника'}
        handleClick={addComponent}
        />
      </div>
    </aside>
  );
}