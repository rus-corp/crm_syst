import React from 'react';

import style from './three_switch.module.css'

export default function ThreeComponentSwitch() {
  const [activeOption, setActiveOption] = React.useState(0)

  function handleChangeOption() {
    setActiveOption(!activeOption)
    // componentSetData(!activeOption)
  }

  return(
    <div className={style.switchWrapper}>
      <div className={style.activeBackground}></div>
      <div className={`${style.wrap} ${activeOption === 0 ? style.active : ''}`}
      onClick={() => setActiveOption(0)}
      >
        <p>Номера</p>
      </div>
      <div className={`${style.wrap} ${activeOption === 1 ? style.active : ''}`}
      onClick={() => setActiveOption(1)}
      >
        <p>Программы</p>
      </div>
      <div className={`${style.wrap} ${activeOption === 2 ? style.active : ''}`}
      onClick={() => setActiveOption(2)}
      >
        <p>История</p>
      </div>
    </div>
  );
}