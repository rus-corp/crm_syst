import React from 'react';

import style from './save_btn.module.css'


export default function SaveBtnComponent({ saveTitle, clicked }) {
  return(
    <button
    className={style.btn}
    type='submit'
    onClick={clicked}
    >
      Сохранить {saveTitle}</button>
  );
}