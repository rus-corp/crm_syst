import React from 'react';

import style from './create_staff.module.css'
import { CreateNewItemBtn } from '../../ui';

import { getStaffs } from '../../api';




export default function CreateStaff() {
  const [staffData, setStaffData] = React.useState(staff)

  const getStaffsList = async() => {
    const response = await getStaffs()
    if (response.status == 200) {
      setStaffData(response.data)
      console.log(response.data)
    }
  }
  React.useEffect(() => {
    getStaffsList()
  }, [])

  return(
    <div className={style.createBlock}>
      <h3>Create Staff</h3>
    </div>
  );
}







