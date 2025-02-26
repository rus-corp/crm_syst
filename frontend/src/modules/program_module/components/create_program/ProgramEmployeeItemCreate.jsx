import React from 'react';

import style from '../styles/create_program.module.css'
import { CreateItemInput, EmployeeSelect } from '../../../../ui';

export default function ProgramEmployeeItemCreate({
  indx,
  staffData,
  handleChangeExpense,
  handleChangeEmpl
}) {
  const handleChangeField = (name, value) => {
    handleChangeExpense(indx, name, value)
  }

  const handleChangeEmployee = (value) => {
    handleChangeEmpl(indx, value)
  }

  return(
    <div className={style.expenseItemHeader}>
      <EmployeeSelect
      dataList={staffData}
      changeFunc={handleChangeEmployee}
      />
      <CreateItemInput
      fieldName={'transfer'}
      changeFunc={handleChangeField}
      />
      <CreateItemInput
      fieldName={'food'}
      changeFunc={handleChangeField}
      />
      <CreateItemInput
      fieldName={'salary'}
      changeFunc={handleChangeField}
      />
      <CreateItemInput
      fieldName={'habitation'}
      changeFunc={handleChangeField}
      />
    </div>
  );
}