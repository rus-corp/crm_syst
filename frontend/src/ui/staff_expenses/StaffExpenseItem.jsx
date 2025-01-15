import React from 'react';

import style from './'
import StaffSelect from '../select/StaffSelect';
import CreateItemInput from '../profile_inputs/CreateItemInput';

export default function Staffexpenseitem({ props }) {
  return(
    <div className={style.expenseItemHeader}>
      <StaffSelect />
      <CreateItemInput />
      <CreateItemInput />
      <CreateItemInput />
      <CreateItemInput />
    </div>
  );
}