import React from 'react';


import style from './styles/company_main.module.css'

import { ExpenseBlock, StaffBlock } from '../index';



export default function CompanyMain() {
  const [programData, setProgramData] = React.useState(programs)
  
  return(
    <section className={style.companyComponent}>
      <div className={style.companyName}>
        <h2>Астроверты</h2>
      </div>
      <div className={style.companyContainer}>
        <div className={style.companyData}>
          <StaffBlock />
          <div className={style.programsBlock}>
            <div className={style.programTitle}>
              <h4>Программы</h4>
              <a>Показать все &gt;</a>
            </div>
            <div className={style.programList}>
              {programData.map((programItem) => (
                <ProgramItemData key={programItem.id}
                programTitle={programItem.title}
                />
              ))}
            </div>
          </div>
        </div>
        <div className={style.usersData}>
          <div className={style.usersBlock}>
              <div className={style.usersHeader}>
                <h4>Пользователи</h4>
                <a>Показать все &gt;</a>
              </div>
              <div className={style.usersList}>
              </div>
          </div>
          <div className={style.usersBlock}>
          <div className={style.usersHeader}>
            <ExpenseBlock />
          </div>
          </div>
        </div>
      </div>
    </section>
  );
}






function ProgramItemData ({ programTitle }) {
  return (
    <div className={style.programItem}>
      <div className={style.programContent}>
        <div className={style.programInfo}>
          <h6>{programTitle}</h6>
        </div>
        <div className={style.programClients}>
          <h6>Клиенты Программы</h6>
        </div>
      </div>
    </div>
  );
}



const programs = [
  {
    "title": "Зимний Байкал",
    "start_date": "2025-01-15",
    "end_date": "2025-01-22",
    "place": "Байкал",
    "desc": "Путешествие к самому глубокому озеру мира зимой.",
    "id": 2,
    "slug": "zimniy-baikal2025-01-15",
    "status": "Active",
    "duration": 7
  },
  {
    "title": "Весенние Карпаты",
    "start_date": "2025-04-10",
    "end_date": "2025-04-17",
    "place": "Карпаты",
    "desc": "Пеший поход по весенним Карпатам с посещением живописных водопадов.",
    "id": 3,
    "slug": "vesennie-karpaty2025-04-10",
    "status": "Upcoming",
    "duration": 7
  },
  {
    "title": "Летняя Камчатка",
    "start_date": "2025-07-05",
    "end_date": "2025-07-14",
    "place": "Камчатка",
    "desc": "Экспедиция на Камчатку с восхождением на вулканы и наблюдением за дикой природой.",
    "id": 4,
    "slug": "letnyaya-kamchatka2025-07-05",
    "status": "Planned",
    "duration": 9
  },
  {
    "title": "Осень в Карелии",
    "start_date": "2025-09-20",
    "end_date": "2025-09-27",
    "place": "Карелия",
    "desc": "Сплав по рекам Карелии среди осенних лесов и озёр.",
    "id": 5,
    "slug": "osen-v-karelii2025-09-20",
    "status": "Draft",
    "duration": 7
  }
]


