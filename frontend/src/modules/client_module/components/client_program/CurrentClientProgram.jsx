import React from 'react';

import style from './styles/current_program.module.css'

import { clientProgramInterface } from '../interfaces/clientProgram';
import { getClientProgramPayments, getClientCurrentProgram } from '../../../../api';
import ClientProgramDetails from '../ui/ClientProgramDetails';
import ClientContractDetailes from '../ui/ClientContractDetailes';
import { formatedStatus, formatedContract } from '../../../../utils';


export default function CurrentClientProgram({ clientId, clientSlug, setProgramId }) {
  const [clientPayments, setClientPayments] = React.useState([])
  const [clientCurrentProgram, setClientCurrentProgram] = React.useState()

  const getClientProgram = async (clientData) => {
    const response = await getClientCurrentProgram(clientData)
    if (response.status === 200) {
      console.log(response.data)
      setProgramId(response.data.program.id)
      setClientCurrentProgram(response.data)
    }
  }

  // const clientProgramPayments = async (clientProgramId) => {
  //   const response = await getClientProgramPayments(clientProgramId)
  //   if (response.status === 200) {
  //     setClientPayments(response.data)
  //   }
  // }

  React.useEffect(() => {
    getClientProgram(clientSlug)
  }, [clientSlug])
  
  return(
    <section className={style.currentClientProgram}>
      <div className={style.clientProgramInfo}>
        <div className={style.programInfoTitle}>
          <h5>Текущая программа</h5>
        </div>
        <div className={style.programInfoDesc}>
          <ClientProgramDetails
          clientId={clientId}
          clientCurrentProgram={clientCurrentProgram?.program?.id}
          clientProgramStatus={formatedStatus(clientCurrentProgram?.status) || ''}
          createdAt={clientCurrentProgram?.created_at}
          />
        </div>
        <div className={style.programInfoDesc}>
          <ClientContractDetailes
          programContractStatus={clientCurrentProgram?.contract_status}
          programPrice={clientCurrentProgram?.price}
          // payments={clientPayments}
          // programPrice={clientProgramData?.price}
          />
        </div>
      </div>
    </section>
  );
}

