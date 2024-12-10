import React from 'react';

import style from './styles/client_program.module.css'
import { SwitchComponent } from '../../../../ui';
import { ThreeComponentSwitch } from '../../../../ui';
import CurrentClientProgram from '../client_program/CurrentClientProgram';
import HistoryClientPorgram from '../client_program/HistoryClientPorgram';



export default function ClientProgram({ programData }) {
  const [option, setOption] = React.useState('Программа')

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
        {option === 'Программа' && <CurrentClientProgram clientProgramData={programData} />}
        {option === 'Проживание'}
        {option === 'История' && <HistoryClientPorgram />}
      </div>
    </section>
  );
}