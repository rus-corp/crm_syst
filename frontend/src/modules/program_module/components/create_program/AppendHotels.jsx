import React from 'react';

import style from '../styles/create_program.module.css'
import { NotificationComponent, CreateItemInput, SaveBtnComponent } from '../../../../ui';


export default function AppendHotels() {
  const [createProgramData, setCreateProgramData] = React.useState({
    title: '',
    start_date: '',
    end_date: '',
    place: '',
    desc: ''
  })
  const [alert, setAlert] = React.useState({severity:'', message:''})
  const handleChange =() => {}
  const handleSubmit = () => {}
  return(
    <section className={style.createProgram}>
      <div className={style.createProgramData}>
        <div className={style.sectionHeader}>
          <h2>Создать Программу</h2>
          <NotificationComponent
          severity={alert.severity}
          message={alert.message}
          />
        </div>
        <div className={style.sectionCreateData}>
          <div className={style.createdField}>
            <CreateItemInput
            fieldTitle='Название программы'
            fieldType='text'
            fieldName='title'
            value={createProgramData.title}
            changeFunc={handleChange}
            />
          </div>
          <div className={style.programDates}>
            <div className={style.programDate}>
              <CreateItemInput
              fieldTitle='Старт Программы'
              fieldType='date'
              fieldWidth='93%'
              fieldName='start_date'
              value={createProgramData.start_date}
              changeFunc={handleChange}
              />
            </div>
            <div className={style.programDate}>
              <CreateItemInput
              fieldTitle='Конец Программы'
              fieldType='date'
              fieldWidth='93%'
              fieldName='end_date'
              value={createProgramData.end_date}
              changeFunc={handleChange}
              />
            </div>
          </div>
          <div className={style.createdField}>
            <CreateItemInput
            fieldTitle='Место'
            fieldType='text'
            fieldName='place'
            value={createProgramData.place}
            changeFunc={handleChange}
            />
          </div>
        </div>
        <div className={style.saveBtn}>
          <SaveBtnComponent
          saveTitle='Программу'
          clicked={handleSubmit}
          />
        </div>
      </div>
    </section>
  );
}