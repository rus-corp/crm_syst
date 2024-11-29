import React from 'react';

import style from './profile_input.module.css'

export default function ProfileInput({ fieldTitle, fieldData }) {
  return(
    <div className={style.infoData}>
      <p>{fieldTitle}</p>
      <input className={style.inputField} type="text" value={fieldData}/>
    </div>
  );
}