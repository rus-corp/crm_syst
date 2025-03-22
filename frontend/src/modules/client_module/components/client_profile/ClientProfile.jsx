import React from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';

import style from './styles/client_profile.module.css'
import ClientProfileData from './ClientProfileData';
import ClientProgram from './ClientProgram';

import { getClientDataWithProgram } from '../../../../api';


export default function ClientProfile() {
  const slug = useSelector((state) => state.client.slug)
  const [clientData, setClientData] = React.useState(
    {
      "id": '',
      "last_name": "",
      "name": "",
      "second_name": "",
      "phone": "",
      "email": "",
      "created_at": "",
      "updated_at": "",
      "slug": "",
      "profile": null,
      "document": null,
      "client_program_detail": []
    }
  )
  
  const getClientData = async(clientSlug) => {
    const response = await getClientDataWithProgram(clientSlug)
    if (response.status == 200) {
      setClientData(response.data)
      console.log(response.data)
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
        clientFirstName={clientData.name}
        clientLastName={clientData.last_name}
        clientSecondName={clientData.second_name}
        createdAt={clientData.created_at}
        phoneNumber={clientData.phone}
        clientCity={clientData.profile?.city}
        clientEmail={clientData.email}
        clientDateOfBirth={clientData.profile?.date_of_birth}
        shortSize={clientData.profile?.shirt_size}
        nutrition={clientData.profile?.nutrition_features}
        comment={clientData.profile?.comment}
        community={clientData.profile?.community}
        clientStatusData={clientData.profile?.status}
        />
        <ClientProgram />
      </div>
    </section>
  );
}