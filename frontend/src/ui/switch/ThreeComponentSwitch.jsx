import React from 'react';

import style from './three_switch.module.css'

export default function ThreeComponentSwitch({ firstData, secondData, thirdData, componentSetData}) {
  const [activeOption, setActiveOption] = React.useState(0)

  function handleChangeOption(data) {
    setActiveOption(data)
    componentSetData(data)
  }

  return(
    <div className={style.switchWrapper}>
      <div className={style.activeBackground}></div>
      <div className={`${style.wrap} ${activeOption === 0 ? style.active : ''}`}
      onClick={() => handleChangeOption(0)}
      >
        <p>{firstData}</p>
      </div>
      <div className={`${style.wrap} ${activeOption === 1 ? style.active : ''}`}
      onClick={() => handleChangeOption(1)}
      >
        <p>{secondData}</p>
      </div>
      <div className={`${style.wrap} ${activeOption === 2 ? style.active : ''}`}
      onClick={() => handleChangeOption(2)}
      >
        <p>{thirdData}</p>
      </div>
    </div>
  );
}