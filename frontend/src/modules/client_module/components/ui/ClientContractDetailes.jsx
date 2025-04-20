import React from 'react';

import style from './styles/clientprofiledetailes.module.css'
import ClientProgramData from './ClientProgramData';
import { SmallButton } from '../../../../ui';
import { formatedContract } from '../../../../utils';

export default function ClientContractDetailes({ programContractStatus, programPrice }) {
  const handleFormatContr = formatedContract(programContractStatus)
  return(
    <div className={style.clientData}>
      <div className={style.clientDataHeader}>
        <h4>Информация по программе</h4>
      </div>
      <div className={style.programContract}>
        <ClientProgramData
        dataTitle={'Договор'}
        data={handleFormatContr}
        />
        {programContractStatus === 'Not Sended' ? (
          <SmallButton
          btnData={'Отправить договор'}
          />
        ) : ''}
      </div>
      <div className={style.clientProgramPrice}>
        <p>Стоимость поездки клиента</p>
        {programPrice === null ? 'Необходимо заселить клиента' : ''}
        <h6>{programPrice}</h6>
      </div>
    </div>
  );
}