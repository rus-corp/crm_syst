import React from 'react';

import style from './small_btn.module.css'


export default function SmallButton({ btnData }) {
  return(
    <div className={style.smallBtn}>
      <button>{btnData}</button>
    </div>
  );
}