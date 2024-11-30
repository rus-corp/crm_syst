import React from 'react';
import { useParams } from 'react-router-dom';

import style from './styles/client_profile.module.css'
import ClientProfileData from './ClientProfileData';
import ClientProgram from './ClientProgram';

import { getClientBySlug } from '../../../../api';


export default function ClientProfile() {
  const { clientSlug } = useParams()
  const [clientProfile, setClientProfile] = React.useState()
  
  const getClientData = async(slug) => {
    const response = await getClientBySlug(slug)
    if (response.status == 200) {
      setClientProfile(response.data)
      console.log(response)
    }
  }

  React.useEffect(() => {
    if (clientSlug) {
      getClientData(clientSlug)
    }
  }, [clientSlug])

  return(
    <section className={style.clientProfileSection}>
      <h2>Профиль клиента</h2>
      <div className={style.clientData}>
        <ClientProfileData props={clientProfile}/>
        <ClientProgram />
      </div>
    </section>
  );
}