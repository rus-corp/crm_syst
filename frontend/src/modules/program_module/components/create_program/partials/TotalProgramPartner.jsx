import React from 'react';

import style from '../../styles/program_total.module.css'
import openList from '@/assets/app_img/open_btn.png'
import { ProfileInput } from '../../../../../ui';



export default function TotalProgramPartner({ partnerData }) {
  const totalExpense = partnerData?.reduce((acc, partner) => {
    return acc + partner.service.price
  }
  , 0)
  const [activeList, setActiveList] = React.useState(false)
  return(
    <section className={style.staticExpenses}>
      <div className={style.expenseHeader}>
        <img
        className={`${activeList ? 'imgOpen' : ''}`}
        src={openList}
        alt="openList"
        onClick={() => setActiveList(!activeList)}
        />
        <h5>Партнеры программы</h5>
        <ProfileInput fieldData={totalExpense}/>
      </div>
      <div className={style.staticExpenseList}>
        {partnerData?.map((partnerItem) => (
          activeList && (
            <PartnerItem key={partnerItem.id}
            partnerTitle={partnerItem.partner.title}
            partnerCategory={partnerItem.partner.category}
            serviceName={partnerItem.service.service_name}
            servicePrice={partnerItem.service.price}
            serviceType={partnerItem.service.service_type}
            />
          )
        ))}
      </div>
    </section>
  );
}


function PartnerItem({ partnerTitle, partnerCategory, serviceName, servicePrice, serviceType }) {
  const handleFormatType = (type) => {
    return serviceTypes[type] || type
  }
  return(
    <div className={style.partnerItem}>
      <div className={style.partnerData}>
        <div className={style.partnerDataContent}>
          <p>Партнер</p>
          <p>Категория</p>
          <p>Услуга</p>
          <p>Стоимость</p>
          <p>Тип цены</p>
        </div>
        <div className={style.partnerDataContent}>
          <span>{partnerTitle}</span>
          <span>{partnerCategory}</span>
          <span>{serviceName}</span>
          <span>{servicePrice}</span>
          <span>{handleFormatType(serviceType)}</span>
        </div>
      </div>
    </div>
  );
}


const serviceTypes = {
  'group': 'Цена за группу',
  'client': 'Цена за человека',
}