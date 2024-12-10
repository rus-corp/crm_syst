import React from 'react';

import style from '../styles/create_program.module.css'

import { CreateItemInput, TextAreaComponent, SaveBtnComponent } from '../../../../ui';

export default function CreateProgramComponent() {
  return(
    <section className={style.createProgram}>
      <div className={style.createProgramData}>
        <div className={style.sectionHeader}>
          <h2>Создать Программу</h2>
        </div>
        <div className={style.sectionCreateData}>
          <div className={style.createdField}>
            <CreateItemInput
            fieldTitle='Название программы'
            fieldType='text'
            />
          </div>
          <div className={style.programDates}>
            <div className={style.programDate}>
              <CreateItemInput
              fieldTitle='Старт Программы'
              fieldType='date'
              fieldWidth='93%'
              />
            </div>
            <div className={style.programDate}>
              <CreateItemInput
              fieldTitle='Конец Программы'
              fieldType='date'
              fieldWidth='93%'
              />
            </div>
          </div>
          <div className={style.createdField}>
            <CreateItemInput
            fieldTitle='Место'
            fieldType='text'
            />
          </div>
          <div className={style.createdField}>
            <TextAreaComponent
            fieldTitle='Описание'
            />
          </div>
          <div className={style.createdField}>
            <CreateItemInput
            fieldTitle='Цена'
            fieldType='number'
            fieldWidth='15rem'
            />
          </div>
        </div>
        <div className={style.saveBtn}>
          <SaveBtnComponent
          saveTitle='Программу'
          />
        </div>
      </div>
    </section>
  );
}