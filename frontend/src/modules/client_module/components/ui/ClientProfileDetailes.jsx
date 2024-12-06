import React from 'react';

import style from './styles/clientprofiledetailes.module.css'


export default function ClientProfileDetailes({ payments, programPrice }) {
  return(
    <div className={style.clientData}>
      <div className={style.clientDataHeader}>
        <h4>Информация по клиенту</h4>
      </div>
      <div className={style.clientPayments}>
        <p>Оплаты клиента:</p>
        {payments.map((payment) => (
          <div className={style.clientPaymentItem}>
            <p>{payment.payment_date}</p>
            <h6>{payment.amount}</h6>
          </div>
        ))}
      </div>
      <div className="clientProgramPrice">
        <p>Стоимость поездки</p>
        <h6>{programPrice}</h6>
      </div>
    </div>
  );
}