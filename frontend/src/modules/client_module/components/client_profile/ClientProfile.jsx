import React from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';

import style from './styles/client_profile.module.css'
import ClientProfileData from './ClientProfileData';
import ClientProgram from './ClientProgram';

import { getClientProfileAndDoc } from '../../../../api';


export default function ClientProfile() {
  const slug = useSelector((state) => state.client.clientSlug)
  const [clientData, setClientData] = React.useState({})
  
  const getClientData = async(clientSlug) => {
    const response = await getClientProfileAndDoc(clientSlug)
    if (response.status == 200) {
      setClientData(response.data)
    }
  }

  React.useEffect(() => {
    if (slug) {
      getClientData(slug)
    }
  }, [slug])

  return(
    <section className={style.clientProfileSection}>
      <h2>Профиль клиента</h2>
      <div className={style.clientData}>
        <ClientProfileData
        clientId={clientData.id}
        clientData={clientData}
        />
        <ClientProgram
        clientId={clientData.id}
        clientSlug={slug}
        />
      </div>
    </section>
  );
}