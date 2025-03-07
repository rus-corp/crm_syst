import React from 'react';

import style from '../styles/partners_main.module.css'
import { ComponentHeaderThreSwitch } from '../../../ui';

export default function PartnerMain() {
  return(
    <div className={style.partnerBlock}>
      <ComponentHeaderThreSwitch
      componentName={'Партнеры'}
      btnName={'Партнера'}
      btnNavi={'create_partner'}
      />
    </div>
  );
}