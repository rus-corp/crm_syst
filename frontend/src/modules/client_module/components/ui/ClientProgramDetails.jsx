import React from 'react';

import style from './styles/clientprogramdetails.module.css'

import { formatedStatus, formatedContract } from '../../../../utils';
import ClientProgramData from './ClientProgramData';
import { SmallButton } from '@/ui';
import { SelectDefComponent } from '../../../../ui';
import { getPrograms, appendClientToProgram } from '../../../../api';
import { ProfileInput, NotificationComponent } from '../../../../ui';

export default function ClientProgramDetails({ clientId, clientCurrentProgram, clientProgramStatus, createdAt }) {
  const [programList, setProgramList] = React.useState([])
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  // const [clientCurrentProgram, setClientCurrentProgram] = React.useState()
  // const clientProgramStatus = formatedStatus(clientProgramData?.status)
  // const clientContractStatus = formatedContract(clientProgramData?.contract_status)
  const handleUpdateClientProgram = async (clientData) => {
    const response = await appendClientToProgram(clientData)
    if (response.status == 201) {
      console.log(response)
      setAlert({severity: 'success', message: response.data})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
      }, 1500);
    }
  }
  const getProgramList = async () => {
    const response = await getPrograms()
    if (response.status === 200) {
      setProgramList(response.data)
    }
  }
  const handleChangeProgram = async (value) => {
    const programData = {
      'program_id': value,
      'client_id': clientId
    }
    handleUpdateClientProgram(programData)
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
          currentDataId={clientCurrentProgram || ''}
          />
        </div>
        <NotificationComponent
        severity={alert.severity}
        message={alert.message}
        />
        <div className={style.clientProgramStatus}>
          <ClientProgramData
          dataTitle={'Статус'}
          data={clientProgramStatus}
          />
          <ClientProgramData
          dataTitle={'Дата заявки'}
          data={createdAt?.slice(0, 10)}
          />
        </div>
        <div className={style.clientProgramdDates}>
          <ProfileInput
          fieldTitle={'Дата начала'}
          fieldType={'date'}
          fieldName={'start_date'}
          />
          <ProfileInput
          fieldTitle={'Дата окончания'}
          fieldType={'date'}
          fieldName={'end_date'}
          />
        </div>
      </div>
    </section>
  );
}