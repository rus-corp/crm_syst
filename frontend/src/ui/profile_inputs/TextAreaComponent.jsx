import React from 'react';

import style from './create_item.module.css'


export default function TextAreaComponent({ fieldTitle }) {
  return(
    <div className={style.createField}>
      <h5>{fieldTitle}</h5>
      <textarea rows={4} cols={50} className={style.inputField} name="" id=""></textarea>
    </div>
  );
}