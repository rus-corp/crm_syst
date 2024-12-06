import React from 'react';

import style from './styles/current_program.module.css'
import { useSelector } from 'react-redux';
import ClientProgramData from '../ui/ClientProgramData';

import { clientProgramInterface } from '../interfaces/clientProgram';
import { getClientProgramPayments } from '../../../../api';
import ClientProgramDetails from '../ui/ClientProgramDetails';
import ClientProfileDetailes from '../ui/ClientProfileDetailes';


export default function CurrentClientProgram({ clientProgramData }) {
  const [clientPayments, setClientPayments] = React.useState([])

  const clientProgramPayments = async (clientProgramId) => {
    const response = await getClientProgramPayments(clientProgramId)
    if (response.status === 200) {
      setClientPayments(response.data)
    }
  }

  React.useEffect(() => {
    if (clientProgramData?.id) {
      clientProgramPayments(clientProgramData.id)
    }
  }, [clientProgramData?.id])
  
  return(
    <section className={style.currentClientProgram}>
      <div className={style.clientProgramInfo}>
        <div className={style.programInfoTitle}>
          <h5>Текущая программа</h5>
        </div>
        <div className={style.programInfoDesc}>
          <ClientProgramDetails
          clientProgramData={clientProgramData ? clientProgramData : clientProgramInterface}
          />
          <ClientProfileDetailes
          payments={clientPayments}
          programPrice={clientProgramData.price}
          />
        </div>
      </div>
    </section>
  );
}

