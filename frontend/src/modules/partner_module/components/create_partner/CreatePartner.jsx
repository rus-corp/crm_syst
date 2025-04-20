import React from 'react';
import { useNavigate } from 'react-router-dom';
import style from '../../styles/create_partner.module.css'
import {
  CreateItemInput,
  SaveBtnComponent,
  SelectDefComponent,
  NotificationComponent,
  SmallButton
} from '../../../../ui';

import { createPartner } from '../../../../api';
import CreatePartnerService from './CreatePartnerService';


const categories = [
  {id: 1, title: "Экскурсии"},
  {id: 2, title: "Трансфер"},
  {id: 3, title: "Остальное"},
]

const serviceType = {
  'true': 'group',
  'false': 'client'
}

export default function CreatePartner() {
  const navigation = useNavigate()
  const [partnerServices, setPartnerServices] = React.useState([{
    service_name: '',
    price: 0,
    service_type: 'group'
  }])
  const [partnerData, setPartnerData] = React.useState({
    title: "",
    law_title: "",
    contract_number: "",
    category: "Экскурсии",
    partner_services: null
  });
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const handleChangeCategory = (value) => {
    setPartnerData((prevData) => ({
      ...prevData,
      category: categories.find((item) => item.id === value).title
    }))
  }

  const handleSubmit = () => {
    const payload = {
      ...partnerData,
      partner_services: partnerServices.filter((item) => (item.price !== 0 && item.service_name !== ''))
    }
    handlecreatePartner(payload)
  }

  const handleChangeServiceData = (indx, name, value) =>{
    if (name === 'service_type') {
      setPartnerServices(
        (prevData) =>
          prevData.map((item, ind) =>
            indx === ind ? {...item, service_type: serviceType[value]} : item)
      )
      return
    }
    setPartnerServices(
      (prevData) => 
        prevData.map((item, ind) => 
        indx === ind ? {...item, [name]: value} : item)
    )
  }
  const handleChangePartnerData = (name, value) => {
    setPartnerData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleAddComponent = () => {
    setPartnerServices((prevData) => [
      ...prevData,
      {
        service_name: '',
        price: 0
      }
    ])
  }

  const handlecreatePartner = async (createdData) => {
    const response = await createPartner(createdData)
    if (response.status === 201) {
      setAlert({severity: 'success', message: 'Партнер успешно добавлен'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
        navigation('/partners')
      }, 1500);
    } else {
      setAlert({severity: 'error', message: 'Ошибка при добавлении партнера'})
    }
  }
  return (
    <section className={style.createPartner}>
      <div className={style.createPartnerData}>
        <div className={style.sectionHeader}>
          <h2>Добавить партнера</h2>
          <NotificationComponent
          severity={alert.severity}
          message={alert.message}
          />
        </div>
        <div className={style.sectionCreateData}>
        <div className={style.createField}>
            <SelectDefComponent
            dataTitle='Категория'
            dataList={categories}
            changeFunc={handleChangeCategory}
            />
          </div>
          <div className={style.createField}>
            <CreateItemInput
            fieldTitle={"Название партнера"}
            fieldName={'title'}
            value={partnerData.title}
            changeFunc={handleChangePartnerData}
            />
          </div>
          <div className={style.createField}>
            <CreateItemInput
            fieldTitle={"Юридическое название"}
            fieldName={'law_title'}
            value={partnerData.law_title}
            changeFunc={handleChangePartnerData}
            />
          </div>
          <div className={style.createField}>
            <CreateItemInput
            fieldTitle={"Номер договора"}
            fieldName={'contract_number'}
            value={partnerData.contract_number}
            changeFunc={handleChangePartnerData}
            />
          </div>
          <div className={style.partnerServicesBlock}>
            {partnerServices.map((serviceItem, indx) => (
              <CreatePartnerService key={indx}
              itemIndx={indx}
              serviceData={serviceItem}
              handleChange={handleChangeServiceData}
              />
            ))}
            <SmallButton
            btnData={'добавить услугу'}
            handleClick={handleAddComponent}
            />
          </div>
          <div className={style.saveBtn}>
            <SaveBtnComponent
            saveTitle='Партнера'
            clicked={handleSubmit}
            />
          </div>
        </div>
      </div>
    </section>
  );
}