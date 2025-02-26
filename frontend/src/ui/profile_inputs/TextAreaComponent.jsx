import React from 'react';

import style from './create_item.module.css'


export default function TextAreaComponent({
  fieldName,
  fieldTitle,
  fieldData,
  handleChange,
  handleKeyDown
}) {
  const handleChangeField = (ev) => {
    const { name, value } = ev.target
    handleChange(name, value)
  }
  return(
    <div className={style.createField}>
      <h5>{fieldTitle}</h5>
      <textarea
      rows={4} cols={50}
      className={style.inputField}
      name={fieldName}
      value={fieldData}
      onChange={handleChangeField}
      onKeyDown={handleKeyDown}
      />
    </div>
  );
}