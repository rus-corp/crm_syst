import React from 'react';

import style from './create_item.module.css'


export default function CreateItemInput({ fieldTitle, fieldType, fieldWidth }) {
  const styles = {
    width: fieldWidth
  }
  return(
    <div className={style.createField}>
      <h5>{fieldTitle}</h5>
      <input className={style.inputField} type={fieldType} style={styles}/>
    </div>
  );
}