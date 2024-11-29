import React from 'react';

import style from './create_btn.module.css'
import add from '../../assets/menu_icons/add.svg'



export default function CreateNewItemBtn({ createDataName }) {
  return(
    <button className={style.createBtn}>
    <img src={add} alt="add" />
      Добавить {createDataName}</button>
  );
}