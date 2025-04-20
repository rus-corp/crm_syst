import React from 'react';
import { Link } from 'react-router-dom';

import style from '../../styles/partner_partials.module.css'


export default function PartnerItem({
  partnerId,
  partnerName,
  partnerLawName,
  partnerServices
}) {
  return(
    <Link to={`/partners/${partnerId}`}>
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
          <div className={style.partnerServiceHeader}>
            <p>Название услуги</p>
            <p>Стоимость услуги</p>
          </div>
          {partnerServices?.map((serviceItem) => (
            <PartnerServiceItem key={serviceItem.id}
            serviceName={serviceItem.service_name}
            servicePrice={serviceItem.price}
            />
          ))}
        </div>
      </div>
    </Link>
  );
}


function PartnerServiceItem({ serviceName, servicePrice }) {
  return (
    <div className={style.partnerServiceItem}>
      <div className={style.serviceName}>
        <h6>{serviceName}</h6>
      </div>
      <div className={style.servicePrice}>
        <h6>{servicePrice}</h6>
      </div>
    </div>
  );
}