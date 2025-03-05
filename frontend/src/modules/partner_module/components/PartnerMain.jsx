import React from 'react';

import style from '../styles/partners_main.module.css'
import { ComponentHeader } from '../../../ui';

export default function PartnerMain() {
  return(
    <div className={style.partnerBlock}>
      <ComponentHeader
      componentName={'Партнеры'}
      />
    </div>
  );
}