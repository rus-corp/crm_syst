import React from 'react';

import style from './main_menu.module.css'
import { ProgramIcon, DashBoardIcon, HotelsIcon, clientIcon, partnersIcon, companyIcon } from '../../ui';
import { MenuItem } from '../../ui';


export default function MainMenu() {
  return(
    <section className={style.menuModule}>
      <div className={style.menu_nav}>
        <MenuItem className={style.menuItem} to='/' label='Сделки' IconComponent={DashBoardIcon} />
        <MenuItem className={style.menuItem} to='/programs' label='Программы' IconComponent={ProgramIcon} />
        <MenuItem className={style.menuItem} to='/hotels' label='Отели' IconComponent={HotelsIcon} />
        <MenuItem className={style.menuItem} to='/clients' label='Клиенты' IconComponent={clientIcon}/>
        <MenuItem className={style.menuItem} to='/partners' label='Партнеры' IconComponent={partnersIcon}/>
        <MenuItem className={style.menuItem} to='/company' label='Компания' IconComponent={companyIcon}/>
      </div>
      <div className={style.menuOption}>
        <h6>Logout</h6>
      </div>
    </section>
  );
}