import React from 'react';

import style from './styles/client_program.module.css'
import { SwitchComponent } from '../../../../ui';
import CurrentClientProgram from '../client_program/CurrentClientProgram';
import HistoryClientPorgram from '../client_program/HistoryClientPorgram';



export default function ClientProgram() {
  const [option, setOption] = React.useState(true)

  const handleChangeoption = (data) => {
    setOption(data)
  }
  return(
    <section className={style.clientProgram}>
      <SwitchComponent
      leftData='Программа'
      rightData='История'
      componentSetData={handleChangeoption}
      />
      <div className={style.clientProgramData}>
        {option ? <CurrentClientProgram /> : <HistoryClientPorgram />}
        
      </div>
    </section>
  );
}