import React from 'react';

import style from '../../styles/program_partner_exp.module.css'


export default function ProgramPartnerseExpense() {
  return(
    <div className={style.programPartnerExpBlock}>
      <div className={style.partnerBlock}>
        <div className={style.partnerItem}>
          <p>услуга</p>
          <p>название партнера</p>
          <input type="text" value={'цена'}/>
        </div>
      </div>
    </div>
  );
}