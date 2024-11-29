import React from 'react';

import style from './styles/programData.module.css'




export default function ProgramComponentData({ programsList, selectedProgram }) {
  const [activeProgram, setActiveProgram] = React.useState(0)

  const handleSelectedProgram = (id, slug) => {
    setActiveProgram(id)
    selectedProgram(slug)
  }


  return(
    <section className={style.programDataList}>
      <div className={style.programDataHeader}>
        <h4>Активные программы</h4>
      </div>
      <div className={style.activeProgramList}>
        {programList.map((program) => (
          <div className={activeProgram == program.id ? `${style.programItem} ${style.activeProgram}` : style.programItem}
          onClick={() => handleSelectedProgram(program.id, program.slug)}
          key={program.id}
          >
            <ActiveProgramItem
            key={program.id}
            programName={program.title}
            programPlace={program.place}
            startDate={program.start_date}
            endDate={program.end_date}
            selectedProgram={selectedProgram}
            />
          </div>
        ))}
      </div>
    </section>
  );
}



function ActiveProgramItem({ programName, programPlace, startDate, endDate }) {
  const handleFormatDate = (dateString) => {
    const dateList = dateString.split('-')
    return `${dateList[2]}-${dateList[1]}-${dateList[0]}`
  }

  

  return (
    <div className={style.programItemData}>
      <p>{programPlace}</p>
      <h5>{programName}</h5>
      <p>с <strong>{handleFormatDate(startDate)}</strong> до <strong>{handleFormatDate(endDate)}</strong></p>
    </div>
  );
}






const programList = [
  {
    "id": 1,
    "title": "Новый год-2025 под звездами Архыза",
    "start_date": "2024-12-29",
    "end_date": "2025-01-03",
    "place": "Архыз",
    "desc": "Чего все ждут с трепетом и особенным предвкушением? Конечно, новогодних праздников и январских каникул!",
    "price": 56000,
    "slug": "novyj-god-2025-pod-zvezdami-arhyza"
  },
  {
    "id": 2,
    "title": "Новый год и Рождество 2025 под Северным сиянием",
    "start_date": "2024-12-30",
    "end_date": "2025-01-03",
    "place": "Мурманская область",
    "desc": "Конфетти, бенгальские огни и искрящиеся букеты фейерверков — самые яркие моменты новогодних каникул",
    "price": 60000,
    "slug": "novyj-god-i-rozhdestvo-2025-pod-severnym-sijaniem"
  },
  {
    "id": 3,
    "title": "Март в Архызе'25",
    "start_date": "2025-02-23",
    "end_date": "2025-03-01",
    "place": "Архыз",
    "desc": "Март в Архызе - интересное время. На ночном небе можно наблюдать как зимний, так и летний Млечный путь!",
    "price": 60000,
    "slug": "mart-v-arhyze25"
  },
  {
    "id": 4,
    "title": "Комета Андромеда",
    "start_date": "2024-11-21",
    "end_date": "2024-11-29",
    "place": "Архыз",
    "desc": "Какое-то описание программы",
    "price": 59000,
    "slug": "kometa-andromeda"
  }
]