import React from 'react';

import style from '../../styles/partner_partials.module.css'


export default function PartnerItem({
  partnerName,
  partnerLawName,
  partnerPrice,
  partnerContract,
  partnerServiceName
}) {
  return(
    <div className={style.partnerItem}>
      <div className={style.partnerMainData}>
        <div className={style.partnerTitle}>
          <p>Название</p>
          <h6>{partnerName}</h6>
        </div>
        <div className={style.partnerLawTitle}>
          <p>Юр. название</p>
          <span>{partnerLawName}</span>
        </div>
      </div>
      <div className={style.partnerContent}>
        <p>Название услуги</p>
        <span>{partnerServiceName}</span>
      </div>
      <div className={style.partnerContent}>
        <p>Стоимость услуг</p>
        <span>{partnerPrice}</span>
      </div>
    </div>
  );
}