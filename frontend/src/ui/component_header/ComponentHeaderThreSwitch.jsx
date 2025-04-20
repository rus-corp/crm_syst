import React from 'react';

import style from './component_header.module.css'
import ThreeComponentSwitch from '../switch/ThreeComponentSwitch';
import CreateNewItemBtn from '../buttons/CreateNewItemBtn';


export default function ComponentHeaderThreSwitch({
  componentName,
  componentDataCount,
  btnName,
  btnNavi,
  handleChangeItem
}) {
  const handleChoiceItem = (data) => {
    handleChangeItem(data)
  }
  return(
    <div className={style.componentHeader}>
      <h3>{componentName} ({componentDataCount})</h3>
      <ThreeComponentSwitch
      firstData={'Экскурсии'}
      secondData={'Трансфер'}
      thirdData={'Остальное'}
      componentSetData={handleChoiceItem}
      />
      <CreateNewItemBtn
      createDataName={btnName}
      navi={btnNavi}
      />
    </div>
  );
}