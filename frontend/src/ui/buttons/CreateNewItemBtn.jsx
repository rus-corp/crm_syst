import React from 'react';
import { useNavigate } from 'react-router-dom';

import style from './create_btn.module.css'
import add from '../../assets/menu_icons/add.svg'



export default function CreateNewItemBtn({ createDataName, navi }) {
  const navigate = useNavigate()
  
  const handleClick = () => {
    navigate(navi)
  }
  return(
    <button className={style.createBtn} onClick={handleClick}>
    <img src={add} alt="add" />
      Добавить {createDataName}</button>
  );
}