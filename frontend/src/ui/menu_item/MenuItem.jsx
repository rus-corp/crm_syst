import React from 'react';

import { NavLink } from 'react-router-dom';
import style from './menu_item.module.css'

import Icon from '../icons/Icon';




export default function MenuItem({ to, label, IconComponent}) {
  return(
    <NavLink
    className={({ isActive}) => 
    isActive ? `${style.menuItem} ${style.active}` : style.menuItem}
    to={to}
    >
      {({ isActive}) => (
        <>
         <Icon isActive={isActive} IconComponent={IconComponent}/>
         <p>{label}</p>
         <div className={style.line}></div>
        </>
      )}
    </NavLink>
  );
}