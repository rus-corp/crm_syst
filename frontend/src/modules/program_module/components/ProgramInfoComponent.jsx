import React from 'react';

import style from './styles/programInfo.module.css'

import { SwitchComponent } from '../../../ui';
import HotelsListComponent from './HotelsListComponent';
import ClientListComponent from './ClientListComponent';




export default function ProgramInfoComponent({ programId }) {
  const [option, setOption] = React.useState(true)

  const handleChangeOption = (data) => {
    setOption(data)
  }

  return(
    <section className={style.programInfoBlock}>
      <div className={style.programBlockHeader}>
        <SwitchComponent
        leftData="Клиенты"
        rightData="Отели"
        componentSetData={handleChangeOption}
        />
      </div>
      {option ? <ClientListComponent programId={programId} /> : <HotelsListComponent programId={programId} />}
      
    </section>
  );
}











