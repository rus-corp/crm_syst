import React from 'react';
import { Link } from 'react-router-dom'
import style from '../styles/company_main.module.css'

import { getStaffs } from '../../../api';


export default function StaffBlock () {
  const [staffData, setStaffData] = React.useState([])

  const getLimitStaffs = async() => {
    const response = await getStaffs(true)
    if (response.status === 200) {
      setStaffData(response.data)
    }
  }

  React.useEffect(() => {
    getLimitStaffs()
  }, [])

  return (
    <div className={style.staffBlock}>
      <div className={style.staffTitle}>
        <h4>Сотрудники</h4>
        <Link to='/company/staff'>Показать всех &gt;</Link>
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
