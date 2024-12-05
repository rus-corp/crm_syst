import React from 'react';

import style from './styles/current_program.module.css'
import { useSelector } from 'react-redux';

import { getClientCurrentProgram } from '../../../../api';


export default function CurrentClientProgram() {
  const [clientCurrentProgram, setClientCurrentProgram] = React.useState({
    "status": "",
    "created_at": "",
    "price": 0,
    "contract_status": "",
    "program": {
        "title": "",
        "start_date": "",
        "end_date": "",
        "place": "",
        "desc": "",
        "price": 0,
        "id": 0,
        "slug": "",
        "status": ""
    }
  })
  const slug = useSelector((state) => state.client.slug)


  const clientProgram = async (clientSlug) => {
    const response = await getClientCurrentProgram(clientSlug)
    if (response.status === 200) {
      setClientCurrentProgram(response.data)
      console.log(response)
    }
  }
  
  React.useEffect(() => {
    if (slug) {
      clientProgram(slug)
    }
  }, [slug])



  return(
    <section className={style.currentClientProgram}>
      <div className={style.clientProgramInfo}>
        <div className={style.programInfoTitle}>
          <h5>Текущая программа</h5>
        </div>
        <div className={style.programInfoDesc}>
          <div className={style.programName}>
            <h4>{clientCurrentProgram.program.title}</h4>
          </div>
          <div className={style.programData}>
            <p>Начало: {clientCurrentProgram.program.start_date}</p>
            <p>Конец: {clientCurrentProgram.program.end_date}</p>
          </div>
        </div>
      </div>
    </section>
  );
}

