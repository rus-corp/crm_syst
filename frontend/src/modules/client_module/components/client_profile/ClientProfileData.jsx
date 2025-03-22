import React from 'react';
import Checkbox from '@mui/material/Checkbox';


import style from './styles/client_profile_data.module.css'
import { ProfileInput } from '../../../../ui';
import { formatedClientStatus } from '../../../../utils';
import { updateClientMainData, updateClientProfileData } from '../../../../api';
import { data } from 'react-router-dom';


export default function ClientProfileData({
  clientId,
  clientFirstName,
  clientLastName,
  clientSecondName,
  createdAt,
  phoneNumber,
  clientStatusData,
  clientCity,
  clientEmail,
  clientDateOfBirth,
  shortSize,
  nutrition,
  comment,
  community=false
}) {
  const [mainData, setMainData] = React.useState({
    phone: phoneNumber,
    email: clientEmail,
  })
  const [profileData, setProfileData] = React.useState({
    city: clientCity,
    date_of_birth: clientDateOfBirth,
    shirt_size: shortSize,
    nutrition_features: nutrition,
    comment: comment
  })
  const [checkedCom, setCheckedCom] = React.useState(community)

  const updateMainData = async (client, updatedData) => {
    const response = await updateClientMainData(client, updatedData)
  }
  const updateProfileData = async (client, updatedData) => {
    const response = await updateClientProfileData(client, updatedData)
  }

  const handleChangeMainData = (ev) => {
    const { name, value } = ev.target
    setMainData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleChangeProfileData = (ev) => {
    const { name, value } = ev.target
    setProfileData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleKeyDownMainData = (ev) => {
    if (ev.key === 'Enter') {
      console.log(mainData)
      updateMainData(clientId, mainData)
    }
  }

  const handleKeyDownProfileData = (ev) => {
    if (ev.key === 'Enter') {
      console.log(profileData)
      updateProfileData(clientId, profileData)
    }
  }

  const handleChangeCommunity = (event) => {
    const newState = event.target.checked;
    setCheckedCom(newState)
    const updatedData = {'community': newState}
    updateProfileData(clientId, updatedData)
  }

  const clientStatus = formatedClientStatus(clientStatusData)

  React.useEffect(() => {
    setCheckedCom(community)
  }, [community])

  return(
    <section className={style.clientProfile}>
      <div className={style.clientFio}>
        <div className={style.clientProfileHeader}>
          <h3>{clientLastName}</h3>
          <h3>{clientFirstName}</h3>
        </div>
        <h6>{clientSecondName}</h6>
        <div className={style.clientCreated}>
          <p>Дата регистрации:</p>
          <p>{createdAt?.slice(0, 10)}</p>
        </div>
        <div className="clientStatus">
          <p>Статус Клиента</p>
          <h6>{clientStatus? clientStatus : ''}</h6>
        </div>
        <div className={style.community}>
          <p>Комьюнити</p>
          <Checkbox checked={checkedCom ?? community} onChange={handleChangeCommunity}/>
        </div>
      </div>
      <div className={style.clientMainInfo}>
        <h5>Информация</h5>
        <ProfileInput
        fieldTitle="Город"
        fieldData={profileData.city ?? clientCity ?? ''}
        fieldName={'city'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
        <ProfileInput 
        fieldTitle="Телефон"
        fieldData={mainData.phone ?? phoneNumber ?? ''}
        fieldType={'number'}
        fieldName={'phone'}
        handleChange={handleChangeMainData}
        handleKeyDown={handleKeyDownMainData}
        />
        <ProfileInput 
        fieldTitle="Email"
        fieldName={'email'}
        fieldData={mainData.email ?? clientEmail ?? ''}
        handleChange={handleChangeMainData}
        handleKeyDown={handleKeyDownMainData}
        />
        <ProfileInput 
        fieldTitle="Дата рождения"
        fieldData={profileData.date_of_birth ?? clientDateOfBirth ?? ''}
        fieldName={'date_of_birth'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        fieldType={'date'}
        />
        <ProfileInput 
        fieldTitle="Питание"
        fieldData={profileData.nutrition_features ?? nutrition ?? ''}
        fieldName={'nutrition_features'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
        <ProfileInput 
        fieldTitle="Размер футболки"
        fieldData={profileData.shirt_size ?? shortSize ?? ''}
        fieldName={'shirt_size'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
        <ProfileInput 
        fieldTitle="Комментарий"
        fieldData={profileData.comment ?? comment ?? ''}
        fieldName={'comment'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
      </div>
    </section>
  );
}