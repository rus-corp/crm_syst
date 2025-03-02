import React from 'react';
import { useNavigate } from 'react-router-dom';
import style from '../styles/create_program.module.css'
import { differenceInCalendarDays } from "date-fns";

import { CreateItemInput, TextAreaComponent, SaveBtnComponent, NotificationComponent } from '@/ui';

import { createProgram } from '@/api';

export default function CreateProgramComponent() {
  const navigation = useNavigate()
  const [createProgramData, setCreateProgramData] = React.useState({
    title: '',
    start_date: '',
    end_date: '',
    place: '',
    desc: ''
  })
  const [alert, setAlert] = React.useState({severity:'', message:''})

  const createNewProgram = async (programData) => {
    const response = await createProgram(programData)
    if (response.status === 201) {
      setAlert({severity: 'success', message: 'Программа создана'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
        navigation(
          'add_hotel', {
            state: {
              programId: response.data.id,
              programTitle: createProgramData.title,
              nights: differenceInCalendarDays(createProgramData.end_date, createProgramData.start_date)
            }
          }
        )
      }, 1500);
    } else {
      setAlert({severity: 'error', message: response.data.detail})
    }
  }

  const handleChange = (name, value) => {
    setCreateProgramData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleSubmit = () => {
    createNewProgram(createProgramData)
    console.log(createProgramData)
  }

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
          <div className={style.createdField}>
            <TextAreaComponent
            fieldTitle='Описание'
            fieldName='desc'
            fieldData={createProgramData.desc}
            handleChange={handleChange}
            // handleKeyDown={}
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