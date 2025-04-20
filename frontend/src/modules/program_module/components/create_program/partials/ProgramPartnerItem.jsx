import React from 'react';

import style from '../../styles/program_hotels.module.css'
import openList from '../../../../../assets/app_img/open_btn.png'
import ProgramPartnerServices from './ProgramPartnerServices';

export default function ProgramPartnerItem({
  partnerId,
  partnerTitle,
  partnerCategory,
  handleAppendServiceToProgram
}) {
  const [activeList, setActiveList] = React.useState(false)
  
  const handleClick = () => setActiveList(!activeList)
  return(
    <>
      <div className={style.serviceData} onClick={handleClick}>
        <div className={style.itemImg}>
          <img className={`${activeList ? 'imgOpen' : ''}`} src={openList} alt="openList" />
        </div>
        <div className={style.hotelTitle}>
          <p>Партнер</p>
          <h5>{partnerTitle}</h5>
        </div>
        <div className={style.hotelAddress}>
          <p>Категория</p>
          <span>{partnerCategory}</span>
        </div>
      </div>
      {activeList && 
        <ProgramPartnerServices
        partnerId={partnerId}
        handleAppendServiceToProgram={handleAppendServiceToProgram}
        />
      }
    </>
  );
}