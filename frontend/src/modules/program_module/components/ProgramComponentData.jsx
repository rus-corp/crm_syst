import React from 'react';

import style from './styles/programData.module.css'




export default function ProgramComponentData({ programsList, selectedProgram }) {
  const [activeProgram, setActiveProgram] = React.useState(0)

  const handleSelectedProgram = (id) => {
    setActiveProgram(id)
    selectedProgram(id)
  }


  return(
    <section className={style.programDataList}>
      <div className={style.programDataHeader}>
        <h4>Активные программы</h4>
      </div>
      <div className={style.activeProgramList}>
        {programsList.map((program) => (
          <div className={activeProgram == program.id ? `${style.programItem} ${style.activeProgram}` : style.programItem}
          onClick={() => handleSelectedProgram(program.id)}
          key={program.id}
          >
            <ActiveProgramItem
            key={program.id}
            programName={program.title}
            programPlace={program.place}
            startDate={program.start_date}
            endDate={program.end_date}
            duration={program.duration}
            />
          </div>
        ))}
      </div>
    </section>
  );
}



function ActiveProgramItem({ programName, programPlace, startDate, endDate, duration }) {
  const handleFormatDate = (dateString) => {
    const dateList = dateString.split('-')
    return `${dateList[2]}-${dateList[1]}-${dateList[0]}`
  }
  
  return (
    <div className={style.programItemData}>
      <p>{programPlace} {duration} д.</p>
      <h5>{programName}</h5>
      <p>с <strong>{handleFormatDate(startDate)}</strong> до <strong>{handleFormatDate(endDate)}</strong></p>
    </div>
  );
}




