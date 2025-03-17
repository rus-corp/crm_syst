import React from 'react';

import style from '../../styles/partner_partials.module.css'


export default function PartnerItem({
  partnerName,
  partnerLawName,
  partnerServices
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
      <div className={style.partnerServicesList}>
        {partnerServices?.map((serviceItem) => (
          <PartnerServiceItem key={serviceItem.id}
          serviceName={serviceItem.service_name}
          servicePrice={serviceItem.price}
          />
        ))}
      </div>
    </div>
  );
}


function PartnerServiceItem({ serviceName, servicePrice }) {
  return (
    <>
      <p>{serviceName}</p>
      <p>{servicePrice}</p>
    </>
  );
}