import React from 'react';

import style from './create_staff.module.css'
import { CreateNewItemBtn } from '../../ui';

import { getStaffs } from '../../api';




export default function StaffBlockComponent() {
  const [staffData, setStaffData] = React.useState([])

  const getStaffsList = async() => {
    const response = await getStaffs()
    if (response.status == 200) {
      setStaffData(response.data)
    }
  }
  React.useEffect(() => {
    getStaffsList()
  }, [])

  return(
    <div className={style.createBlock}>
      <div className={style.blockHeader}>
        <h2>Сотрудники</h2>
        <CreateNewItemBtn
        createDataName='Сотрудника'
        navi={'/create_item/create_staff'}
        />
      </div>
      <div className={style.blockContent}>
        {staffData.map((staffItem) => (
          <StaffItem key={staffItem.id}
          staffName={staffItem.first_name}
          staffLastName={staffItem.last_name}
          staffPosition={staffItem.position}
          staffComment={staffItem.comment}
          staffExpense={staffItem.expenses}
          />
        ))}
      </div>
    </div>
  );
}


function StaffItem ({ staffName, staffLastName, staffPosition, staffComment, staffExpense }) {
  return (
    <div className={style.staffItem}>
      <div className={style.staffMainData}>
        <div className={style.staffHeader}>
          <div className={style.staffName}>
            <p>Имя</p>
            <h6>{staffName}</h6>
          </div>
          <div className={style.staffLastName}>
            <p>Фамилия</p>
            <h6>{staffLastName}</h6>
          </div>
        </div>
        <div className={style.staffContent}>
          <div className={style.staffPosition}>
            <p>Должность</p>
            <h6>{staffPosition}</h6>
            <p>Комментарий</p>
            <h6>{staffComment}</h6>
          </div>
        </div>
      </div>
      <div className='line'></div>
      <div className={style.staffExpenses}>
        {staffExpense?.map((staffExpenseItem) => (
          <div className={style.staffExpenseItem} key={staffExpenseItem.id}>
            <p>{staffExpenseItem.category.title}</p>
            <h6>{staffExpenseItem.amount}</h6>
          </div>
        ))}
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


{/* <div className={style.staffHeader}>
<h6>{staffName}</h6>
<h6>{staffLastName}</h6>
</div>
<div className={style.staffContent}>
<div className={style.staffPosition}>
  <p>{staffPosition}</p>
  <p>{staffComment}</p>
</div>
<div className={style.staffExpenses}>
  {staffExpense?.map((staffExpenseItem) => (
    <p key={staffExpenseItem.id}>{staffExpenseItem.amount}</p>
  ))}
</div>
</div> */}