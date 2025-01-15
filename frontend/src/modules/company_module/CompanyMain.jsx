import React from 'react';

import style from './styles/company_main.module.css'


export default function CompanyMain() {
  const [staffData, setStaffData] = React.useState(staff)
  const [programData, setProgramData] = React.useState(programs)
  return(
    <section className={style.companyComponent}>
      <div className={style.companyContainer}>
        <div className={style.companyData}>
          <div className={style.companyName}>
            <h2>Астроверты</h2>
          </div>
          <div className={style.staffBlock}>
            <div className={style.staffTitle}>
              <h4>Сотрудники</h4>
              <a>Показать всех &gt;</a>
            </div>
            <div className={style.staffList}>
              {staffData.map((staffItem) => (
                <StaffItem key={staffItem.id}
                staffName={staffItem.first_name}
                staffLastName={staffItem.last_name}
                staffPos={staffItem.position}
                />
              ))}
            </div>
          </div>
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
      </div>
    </section>
  );
}



function StaffItem({staffName, staffLastName, staffPos}) {
  return (
    <div className={style.staffItem}>
      <div className={style.staffName}>
        <h6>{staffName} {staffLastName}</h6>
      </div>
      <div className={style.staffPos}>
        <p>{staffPos}</p>
      </div>
    </div>
  );
}


function ProgramItemData ({ programTitle }) {
  return (
    <div className={style.programItem}>
      <div className={style.programContent}>
        <p>{programTitle}</p>
      </div>
    </div>
  );
}


const staff = [
  {
    "first_name": "Иван",
    "last_name": "Иванов",
    "position": "Менеджер проекта",
    "id": 1
  },
  {
    "first_name": "Марина",
    "last_name": "Петрова",
    "position": "Главный бухгалтер",
    "id": 2
  },
  {
    "first_name": "Алексей",
    "last_name": "Кузнецов",
    "position": "Старший разработчик",
    "id": 3
  },
  {
    "first_name": "Ольга",
    "last_name": "Смирнова",
    "position": "HR-менеджер",
    "id": 4
  },
  {
    "first_name": "Дмитрий",
    "last_name": "Васильев",
    "position": "Директор по маркетингу",
    "id": 5
  },
  {
    "first_name": "Дмитрий",
    "last_name": "Васильев",
    "position": "Директор по маркетингу",
    "id": 6
  },
  {
    "first_name": "Дмитрий",
    "last_name": "Васильев",
    "position": "Директор по маркетингу",
    "id": 7
  },
  {
    "first_name": "Дмитрий",
    "last_name": "Васильев",
    "position": "Директор по маркетингу",
    "id": 8
  },
]


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
  },
  {
    "title": "Новогоднее путешествие на Алтай",
    "start_date": "2025-12-30",
    "end_date": "2026-01-06",
    "place": "Алтай",
    "desc": "Встреча Нового года на Алтае с катанием на лыжах и экскурсией по природным достопримечательностям.",
    "id": 6,
    "slug": "novogodnee-puteshestvie-na-altai2025-12-30",
    "status": "Future",
    "duration": 7
  }
]


