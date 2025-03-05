import React from 'react';

import style from './small_btn.module.css'


export default function SmallButton({ btnData, handleClick }) {
  return(
    <div className={style.smallBtn}>
      <button onClick={handleClick}>{btnData}</button>
    </div>
  );
}