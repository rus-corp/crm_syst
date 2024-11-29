import React from 'react';

import style from './switch.module.css'



export default function SwitchComponent({ leftData, rightData, componentSetData }) {
  const [activeOption, setActiveOption] = React.useState(true)

  function handleChangeOption() {
    setActiveOption(!activeOption)
    componentSetData(!activeOption)
  }

  return(
    <div className={style.switchWrapper} onClick={handleChangeOption}>
      <div className={`${style.activeBackground} ${activeOption ? style.activeLeft : style.activeRight}`}></div>
      <div className={style.wrap}>
        <p>{leftData}</p>
      </div>
      <div className={style.wrap}>
        <p>{rightData}</p>
      </div>
    </div>
  );
}