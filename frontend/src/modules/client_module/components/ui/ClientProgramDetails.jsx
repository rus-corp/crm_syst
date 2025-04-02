import React from 'react';

import style from './styles/clientprogramdetails.module.css'

import { formatedStatus, formatedContract } from '../../../../utils';
import ClientProgramData from './ClientProgramData';
import { SmallButton } from '@/ui';
import { SelectDefComponent } from '../../../../ui';
import { getPrograms } from '../../../../api';
import { ProfileInput } from '../../../../ui';

export default function ClientProgramDetails({ clientProgramData }) {
  const [programList, setProgramList] = React.useState([])
  const [clientCurrentProgram, setClientCurrentProgram] = React.useState()
  const clientProgramStatus = formatedStatus(clientProgramData?.status)
  const clientContractStatus = formatedContract(clientProgramData?.contract_status)

  const getProgramList = async () => {
    const response = await getPrograms()
    if (response.status === 200) {
      setProgramList(response.data)
    }
  }
  const handleChangeProgram = (value) => {
    console.log(value)
  }

  React.useEffect(() => {
    getProgramList()
  }, [])

  return(
    <section className={style.clientCurrentProgram}>
      <div className={style.programData}>
        <div className={style.programTitle}>
          <p>Программа клиента</p>
          <SelectDefComponent
          dataList={programList}
          dataTitle={'Программа'}
          changeFunc={handleChangeProgram}
          />
        </div>
        <div className={style.clientProgramStatus}>
          <ClientProgramData
          dataTitle={'Статус'}
          />
        </div>
        <div className={style.clientProgramdDates}>
          <ProfileInput
          fieldTitle={'Дата заезда'}
          fieldType={'date'}
          fieldName={'start_date'}
          />
          <ProfileInput
          fieldTitle={'Дата выезда'}
          fieldType={'date'}
          fieldName={'end_date'}
          />
        </div>
      </div>
    </section>
    // <div className={style.programData}>
    //   <div className={style.programName}>
    //     <h4>{clientProgramData.program.title}</h4>
    //   </div>
    //   <div className={`${style.programDataItem} ${style.programDates}`}>
    //     <div className={style.programDate}>
    //       <p>Начало:</p>
    //       <h6>{clientProgramData.program.start_date}</h6>
    //     </div>
    //     <div className={style.programDate}>
    //       <p>Конец:</p>
    //       <h6>{clientProgramData.program.end_date}</h6>
    //     </div>
    //   </div>
    //   <ClientProgramData
    //   dataTitle='Статус клиента'
    //   data={clientProgramStatus}
    //   />
    //   <ClientProgramData
    //   dataTitle='Стоимость программы'
    //   data={clientProgramData.program.price}
    //   />
    //   <div className={style.contractData}>
    //     <ClientProgramData
    //     dataTitle='Договор'
    //     data={clientContractStatus}
    //     />
    //     {clientProgramData?.contract_status === 'Not Sended' ? (
    //       <SmallButton
    //       btnData='Отправить договор'
    //       />
    //     ): ''}
    //   </div>
    //   <ClientProgramData
    //   dataTitle='Дата заявки'
    //   data={clientProgramData.created_at.slice(0, 10)}
    //   />
    // </div>
  );
}