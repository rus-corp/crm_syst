import React from 'react';

import style from './styles/client_program_data.module.css'


export default function ClientProgramData({ dataTitle, data}) {
  return(
    <div className={`${style.programDataItem} ${style.clientRegisterDate}`}>
      <p>{dataTitle}:</p>
      <h6>{data}</h6>
    </div>
  );
}