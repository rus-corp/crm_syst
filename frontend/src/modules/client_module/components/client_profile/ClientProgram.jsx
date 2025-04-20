import React from 'react';

import style from './styles/client_program.module.css'
import { SwitchComponent } from '../../../../ui';
import { ThreeComponentSwitch } from '../../../../ui';
import CurrentClientProgram from '../client_program/CurrentClientProgram';
import HistoryClientPorgram from '../client_program/HistoryClientPorgram';
import ClientProgramHotels from '../client_program/ClientProgramHotels';



export default function ClientProgram({ clientId, clientSlug }) {
  const [option, setOption] = React.useState('Программа')
  const [clientProgramId, setClientProgramId] = React.useState(null)

  const handleChangeOption = (data) => {
    if (data === 0) {
      setOption('Программа')
    } else if (data === 1) {
      setOption('Проживание')
    } else if (data === 2) {
      setOption('История')
    }
  }
  return(
    <section className={style.clientProgram}>
      <ThreeComponentSwitch
      firstData='Программа'
      secondData='Проживание'
      thirdData='История'
      componentSetData={handleChangeOption}
      />
      <div className={style.clientProgramData}>
        {option === 'Программа' && (
          <CurrentClientProgram
          clientId={clientId}
          clientSlug={clientSlug}
          setProgramId={setClientProgramId} />
        )}
        {option === 'Проживание' && <ClientProgramHotels programId={clientProgramId} />}
        {option === 'История' && <HistoryClientPorgram />}
      </div>
    </section>
  );
}