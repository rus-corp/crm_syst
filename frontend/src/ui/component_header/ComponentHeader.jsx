import React from 'react';

import CreateNewItemBtn from '../buttons/CreateNewItemBtn';
import style from './component_header.module.css'
import SwitchComponent from '../switch/SwitchComponent';




export default function ComponentHeader({
  componentName,
  componentDataCount,
  componentSetData,
  btnName,
  btnNavi
}) {
  return(
    <div className={style.componentHeader}>
      <h3>{componentName} ({componentDataCount})</h3>
      <SwitchComponent
      leftData="Список"
      rightData="Карточки"
      componentSetData={componentSetData} />
      <CreateNewItemBtn
      createDataName={btnName}
      navi={btnNavi}
      />
    </div>

  );
}