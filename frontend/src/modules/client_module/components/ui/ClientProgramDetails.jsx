import React from 'react';

import style from './styles/clientprogramdetails.module.css'

import { formatedStatus, formatedContract } from '../../../../utils';
import ClientProgramData from './ClientProgramData';

export default function ClientProgramDetails({ clientProgramData }) {
  const clientProgramStatus = formatedStatus(clientProgramData?.status)
  const clientContractStatus = formatedContract(clientProgramData?.contract_status)

  return(
    <div className={style.programData}>
      <div className={style.programName}>
        <h4>{clientProgramData.program.title}</h4>
      </div>
      <div className={`${style.programDataItem} ${style.programDates}`}>
        <div className={style.programDate}>
          <p>Начало:</p>
          <h6>{clientProgramData.program.start_date}</h6>
        </div>
        <div className={style.programDate}>
          <p>Конец:</p>
          <h6>{clientProgramData.program.end_date}</h6>
        </div>
      </div>
      <ClientProgramData
      dataTitle='Статус клиента'
      data={clientProgramStatus}
      />
      <ClientProgramData
      dataTitle='Стоимость программы'
      data={clientProgramData.program.price}
      />
      <ClientProgramData
      dataTitle='Договор'
      data={clientContractStatus}
      />
      <ClientProgramData
      dataTitle='Дата заявки'
      data={clientProgramData.created_at.slice(0, 10)}
      />
    </div>
  );
}