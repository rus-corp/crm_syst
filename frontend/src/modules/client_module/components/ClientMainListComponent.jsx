import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import style from './client_module.module.css'
import ClientProfile from './client_profile/ClientProfile';
import ClientProgram from './client_profile/ClientProgram';
import { setClientSlug } from '../../../store/clientSlice';

import { getClientList } from '../../../api';



export default function ClientMainListComponent() {
  const [clientList, setClientList] = React.useState([])
  const getClients = async () => {
    const response = await getClientList();
    if (response.status === 200) {
      setClientList(response.data);
    }
  }
  React.useEffect(() => {
    getClients();
  }, [])
  return(
    <section className={style.clientSection}>
      <div className={style.clientData}>
        <div className={style.clientSectionHeader}>
          <h2>Клиенты</h2>
        </div>
        <div className={style.clientSectionList}>
          {clientList.map((client) => (
            <ClientItem key={client.id}
            clientLastName={client.last_name}
            clientName={client.name}
            clientSecondName={client.second_name}
            clientPhone={client.phone}
            clientEmail={client.email}
            clientCreated={client.created_at}
            clientSlug={client.slug}
            />
          ))}
        </div>
      </div>
    </section>
  );
}



function ClientItem({
  clientLastName,
  clientName,
  clientSecondName,
  clientPhone,
  clientEmail,
  clientCreated,
  clientSlug
}) {
  const dispatch = useDispatch();
  const handleFormatDate = (dateString) => {
    const dateList = dateString.split('T')
    const date = dateList[0].split('-')
    return `${date[2]}.${date[1]}.${date[0]}`
  }
  
  return (
    <Link
    to={`/clients/${clientSlug}`}
    onClick={() => dispatch(setClientSlug(clientSlug))}
    className={style.clientItem}>
      <div className={style.clientDataItem}>
        <p>Фамилия и Имя клиента</p>
        <h5>{clientLastName} {clientName}</h5>
      </div>
      <div className={style.clientDataItem}>
        <p>Номер телефона</p>
        <span>{clientPhone}</span>
      </div>
      <div className={style.clientDataItem}>
        <p>Email клиента</p>
        <span>{clientEmail}</span>
      </div>
      <div className={style.clientDataItem}>
        <p>Дата регистрации</p>
        <span>{handleFormatDate(clientCreated)}</span>
      </div>
    </Link>
  );
}