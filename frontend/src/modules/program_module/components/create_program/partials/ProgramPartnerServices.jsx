import React from 'react';

import style from '../../styles/hotelRooms.module.css'
import { getPartnerByIdWithServiceAndBank } from '../../../../../api';


export default function ProgramPartnerServices({ partnerId, handleAppendServiceToProgram }) {
  const [partnerServices, setPartnerServices] = React.useState([])
  const getPartnerServices = async (partnerData) => {
    const response = await getPartnerByIdWithServiceAndBank(partnerData)
    if (response.status === 200) {
      setPartnerServices(response.data.partner_services)
    }
  }

  const handleAppendService = (serviceId, state) => {
    handleAppendServiceToProgram(partnerId, serviceId, state)
  }

  React.useEffect(() => {
    getPartnerServices(partnerId)
  }, [partnerId])

  return(
    <div className={style.hotelRoomsList}>
      <div className={style.hotelRoomHeader}>
        <p></p>
        <p>Описание</p>
        <p>Стоимость</p>
      </div>
      {partnerServices.map((serviceItem) => (
        <ServiceItem key={serviceItem.id}
        serviceId={serviceItem.id}
        serviceName={serviceItem.service_name}
        servicePrice={serviceItem.price}
        handleAppendService={handleAppendService}
        />
      ))}
    </div>
  );
}


function ServiceItem({ serviceId, serviceName, servicePrice, handleAppendService }) {
  const [isSelected, setIsSelected] = React.useState(false)
  const appendServiceToProgram = () => {
    const newState = !isSelected
    setIsSelected(newState)
    handleAppendService(serviceId, newState)
  }
  return (
    <div className={style.roomItem}>
      <input type="checkbox" checked={isSelected} onChange={() => appendServiceToProgram()}/>
      <span>{serviceName}</span>
      <span>{servicePrice}</span>
    </div>
  );
}