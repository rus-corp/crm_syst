import React from 'react';

import style from './save_btn.module.css'


export default function SaveBtnComponent({ saveTitle}) {
  return(
    <button
    className={style.btn}
    type='submit'>
      Сохранить {saveTitle}</button>
  );
}