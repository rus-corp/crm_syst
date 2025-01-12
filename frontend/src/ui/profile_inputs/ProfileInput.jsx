import React from 'react';

import style from './profile_input.module.css'

export default function ProfileInput({
  fieldName,
  fieldType,
  fieldTitle,
  fieldData,
  handleChange,
  handleKeyDown
}) {
  
  const handleChangeField = (ev) => {
    handleChange(ev)
  }
  
  return(
    <div className={style.infoData}>
      <p>{fieldTitle}</p>
      <input className={style.inputField}
      type={fieldType}
      value={fieldData}
      name={fieldName}
      onChange={handleChangeField}
      onKeyDown={handleKeyDown}
      />
    </div>
  );
}