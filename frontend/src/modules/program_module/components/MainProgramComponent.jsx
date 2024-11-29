import React from 'react';

import style from './styles/mainProgramComponent.module.css'

import ProgramComponentData from './ProgramComponentData';
import ProgramInfoComponent from './ProgramInfoComponent';
import { CreateNewItemBtn } from '../../../ui';

import { getPrograms } from '../../../api';



export default function MainProgramComponent() {
  const [selectedProgram, setSelectedProgram] = React.useState('')
  const [programsData, setProgramsData] = React.useState([])

  const getProgarmsData = async() => {
    const response = await getPrograms()
    if (response.status == 200) {
      setProgramsData(response.data)
    }
  }

  React.useEffect(() => {
    getProgarmsData()
  }, [])
  
  const handleSelectProgram = (data) => {
    setSelectedProgram(data)
  }
  return(
    <section className={style.programMainContainer}>
      <div className={style.programHeader}>
        <h2>Программы</h2>
        <CreateNewItemBtn
        createDataName='Программу'
        />
      </div>
      <div className={style.programDataContainer}>
        <ProgramComponentData
        selectedProgram={handleSelectProgram}
        programsList={programsData}
        />
        <ProgramInfoComponent programId={selectedProgram}/>
      </div>
    </section>
  );
}