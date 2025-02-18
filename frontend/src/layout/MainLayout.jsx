import React from 'react';

import style from './layout.module.css'


export default function MainLayout({ children }) {
  return(
    <div className={style.layoutBlock}>
      {children}
    </div>
  );
}