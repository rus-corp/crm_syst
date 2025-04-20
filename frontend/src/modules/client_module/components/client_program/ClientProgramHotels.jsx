import React from 'react';

import style from './styles/program_hotels.module.css'
import { getProgramHotelRooms } from '../../../../api';


export default function ClientProgramHotels({ programId }) {
  const handleProgramRooms = async (programData) => {
    const response = await getProgramHotelRooms(programData)
    console.log(response.data)
  }

  React.useEffect(() => {
    handleProgramRooms(programId)
  }, [])
  return(
    <section className={style.currentClientProgram}>
      <div className={style.clientProgramInfo}>
        <div className={style.programInfoTitle}>
          <h5>Текущее проживание</h5>
        </div>
      </div>
      <div className={style.programHotelDesc}>

      </div>
    </section>
  );
}