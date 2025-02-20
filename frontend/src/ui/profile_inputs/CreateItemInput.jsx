import React from 'react';

import style from './create_item.module.css'


export default function CreateItemInput({
  fieldTitle,
  fieldType,
  fieldWidth,
  fieldName,
  value,
  changeFunc
}) {
  const styles = {
    width: fieldWidth
  }

  const handleChange = (ev) => {
    const { name, value } = ev.target
    console.log(name, value)
    changeFunc(name, value)
  }

  return(
    <div className={style.createField}>
      <h5>{fieldTitle}</h5>
      <input 
      className={style.inputField}
      type={fieldType}
      style={styles}
      name={fieldName}
      onChange={handleChange}
      value={value}
      />
    </div>
  );
}