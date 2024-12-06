import React from 'react';
import { Link } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import style from './styles/clientInfo.module.css'
import { handleClientCount, handleContractCount } from '../helpers';
import { formatedContract, formatedStatus } from '../../../utils';

import { getProgramClients } from '../../../api';
import { setClientSlug } from '../../../store/clientSlice';


export default function ClientListComponent({ programId }) {
  const [clientList, setClientList] = React.useState([])
  const handleGetProgramClients = async (slug) => {
    const response = await getProgramClients(slug)
    if (response.status === 200) {
      setClientList(response.data.program_clients_detail)
    }
  }

  const {PF, CF, NC} = handleClientCount(clientList)
  const contractCount = handleContractCount(clientList)
  
  React.useEffect(() => {
    if (programId) {
      handleGetProgramClients(programId)
    }
  }, [programId])

  return(
    <section className={style.programClients}>
      <div className={style.confirmedClients}>
        <div className={style.confirmedClientsHeader}>
          <div className={style.clientHeaderData}>
            <p>Аванс Оплачен</p>
            <h6>{CF}</h6>
          </div>
          <div className={style.clientHeaderData}>
            <p>Полная оплата</p>
            <h6>{PF}</h6>
          </div>
          <div className={style.clientHeaderData}>
            <p>Думают</p>
            <h6>{NC}</h6>
          </div>
          <div className={style.clientHeaderData}>
            <p>Подписан догвор</p>
            <h6>{contractCount}</h6>
          </div>
        </div>
        <div className={style.clientList}>
          {clientList.map((clientItem) => (
            <ClientItem key={clientItem.client.id}
            clientLastName={clientItem.client.last_name}
            clientName={clientItem.client.name}
            clientPhone={clientItem.client.phone}
            createdDate={clientItem.client.created_at.slice(0, 10)}
            contractStatus={clientItem.client.contract_status}
            clientPrice={clientItem.price}
            clientStatus={clientItem.status}
            clientSlug={clientItem.client.slug}
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
  clientPhone,
  contractStatus,
  createdDate,
  clientPrice,
  clientStatus,
  clientSlug
}) {
  const dispatch = useDispatch()

  return (
    <Link
    to={`/clients/${clientSlug}`}
    className={style.clientItem}
    onClick={() => dispatch(setClientSlug(clientSlug))}>
      
      <div className={style.clientFullName}>
        <p>{clientName}</p>
        <h5>{clientLastName}</h5>
      </div>
      <div className={style.clientitemData}>
        <p>Телефон</p>
        <h6>{clientPhone}</h6>
      </div>
      <div className={style.clientitemData}>
        <p>Регистрация</p>
        <h6>{createdDate}</h6>
      </div>
      <div className={style.clientitemData}>
        <p>Договор</p>
        <h6>{formatedContract(contractStatus)}</h6>
      </div>
      <div className={style.clientitemData}>
        <p>Цена программы</p>
        <h6>{clientPrice}</h6>
      </div>
      <div className={style.clientitemData}>
        <p>Статус</p>
        <h6>{formatedStatus(clientStatus)}</h6>
      </div>
    </Link>
  );
}


