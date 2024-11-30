import React from 'react';

import style from './styles/current_program.module.css'


export default function CurrentClientProgram() {
  return(
    <section className={style.currentClientProgram}>
      <div className={style.clientProgramInfo}>
        <div className={style.programInfoTitle}>
          <h5>Текущая программа</h5>
        </div>
        <div className={style.programInfoDesc}>
          <div className={style.programName}>
            <h4>Program Name</h4>
          </div>
          <div className={style.programData}>
            <p>Start: 2024-11-30</p>
            <p>End: 2024-11-30</p>
          </div>
        </div>
      </div>
    </section>
  );
}