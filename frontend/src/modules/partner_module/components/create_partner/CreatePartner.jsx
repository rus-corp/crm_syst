import React from 'react';
import { useNavigate } from 'react-router-dom';
import style from '../../styles/create_partner.module.css'
import {
  CreateItemInput,
  SaveBtnComponent,
  SelectDefComponent,
  NotificationComponent
} from '../../../../ui';

import { createPartner } from '../../../../api';


const categories = [
  {id: 1, title: "Экскурсии"},
  {id: 2, title: "Трансфер"},
  {id: 3, title: "Остальное"},
]


export default function CreatePartner() {
  const navigation = useNavigate()
  const [partnerData, setPartnerData] = React.useState({
    title: "",
    law_title: "",
    price: '',
    contract_number: "",
    service_name: "",
    category: "Экскурсии"
  });
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const handleChangeCategory = (value) => {
    setPartnerData((prevData) => ({
      ...prevData,
      category: categories.find((item) => item.id === value).title
    }))
  }
  const handleSubmit = () => {
    handlecreatePartner(partnerData)
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

  const handleChangePartnerField = (name, value) => {
    setPartnerData((prevData) => ({
      ...prevData,
      [name]: value
    }))
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
            <CreateItemInput
            fieldTitle={"Название партнера"}
            fieldName={'title'}
            value={partnerData.title}
            changeFunc={handleChangePartnerField}
            />
          </div>
          <div className={style.createField}>
            <CreateItemInput
            fieldTitle={"Юридическое название"}
            fieldName={'law_title'}
            value={partnerData.law_title}
            changeFunc={handleChangePartnerField}
            />
          </div>
          <div className={style.createField}>
            <CreateItemInput
            fieldTitle={"Прайс"}
            fieldName={'price'}
            value={partnerData.price}
            changeFunc={handleChangePartnerField}
            />
          </div>
          <div className={style.createField}>
            <CreateItemInput
            fieldTitle={"Услуга"}
            fieldName={'service_name'}
            value={partnerData.service_name}
            changeFunc={handleChangePartnerField}
            />
          </div>
          <div className={style.createField}>
            <CreateItemInput
            fieldTitle={"Номер договора"}
            fieldName={'contract_number'}
            value={partnerData.contract_number}
            changeFunc={handleChangePartnerField}
            />
          </div>
          <div className={style.createField}>
            <SelectDefComponent
            dataTitle='Категория'
            dataList={categories}
            changeFunc={handleChangeCategory}
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