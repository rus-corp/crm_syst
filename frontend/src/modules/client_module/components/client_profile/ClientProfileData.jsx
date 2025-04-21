import React from 'react';
import Checkbox from '@mui/material/Checkbox';


import style from './styles/client_profile_data.module.css'
import { ProfileInput } from '../../../../ui';
import { formatedClientStatus } from '../../../../utils';
import { updateClientMainData, updateClientProfileData } from '../../../../api';



export default function ClientProfileData({ clientData, clientId }) {
  const [mainData, setMainData] = React.useState({
    phone: clientData.phone || null,
    email: clientData.email || null,
  })
  const [profileData, setProfileData] = React.useState({
    city: clientData.profile?.city || null,
    date_of_birth: clientData.profile?.date_of_birth || null,
    shirt_size: clientData.profile?.shirt_size || null,
    nutrition_features: clientData.profile?.nutrition_features || null,
    comment: clientData.profile?.comment || null,
    community: clientData.profile?.date_of_birth || null
  })

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
    const newData = {'community': newState}
    setProfileData((prevData) => ({
      ...prevData,
      community: newState
    }))
    updateProfileData(clientId, newData)
  }

  const clientStatus = formatedClientStatus(clientData.profile?.status)

  return(
    <section className={style.clientProfile}>
      <div className={style.clientFio}>
        <div className={style.clientProfileHeader}>
          <h3>{clientData.last_name}</h3>
          <h3>{clientData.name}</h3>
        </div>
        <h6>{clientData.second_name}</h6>
        <div className={style.clientCreated}>
          <p>Дата регистрации:</p>
          <p>{clientData.created_at?.slice(0, 10)}</p>
        </div>
        <div className="clientStatus">
          <p>Статус Клиента</p>
          <h6>{clientStatus}</h6>
        </div>
        <div className={style.community}>
          <p>Комьюнити</p>
          <Checkbox checked={profileData.community || clientData.profile?.community || false} onChange={handleChangeCommunity}/>
        </div>
      </div>
      <div className={style.clientMainInfo}>
        <h5>Информация</h5>
        <ProfileInput
        fieldTitle="Город"
        fieldData={profileData.city || clientData.profile?.city || ''}
        fieldName={'city'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
        <ProfileInput 
        fieldTitle="Телефон"
        fieldData={mainData.phone || clientData.phone || ''}
        fieldType={'number'}
        fieldName={'phone'}
        handleChange={handleChangeMainData}
        handleKeyDown={handleKeyDownMainData}
        />
        <ProfileInput 
        fieldTitle="Email"
        fieldName={'email'}
        fieldData={mainData.email || clientData.email || ''}
        handleChange={handleChangeMainData}
        handleKeyDown={handleKeyDownMainData}
        />
        <ProfileInput 
        fieldTitle="Дата рождения"
        fieldData={profileData.date_of_birth || clientData.profile?.date_of_birth || ''}
        fieldName={'date_of_birth'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        fieldType={'date'}
        />
        <ProfileInput 
        fieldTitle="Питание"
        fieldData={profileData.nutrition_features || clientData.profile?.nutrition_features || ''}
        fieldName={'nutrition_features'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
        <ProfileInput 
        fieldTitle="Размер футболки"
        fieldData={profileData.shirt_size || clientData.profile?.shirt_size || ''}
        fieldName={'shirt_size'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
        <ProfileInput 
        fieldTitle="Комментарий"
        fieldData={profileData.comment || clientData.profile?.comment || ''}
        fieldName={'comment'}
        handleChange={handleChangeProfileData}
        handleKeyDown={handleKeyDownProfileData}
        />
      </div>
    </section>
  );
}