import React from 'react';

import style from './create_staff.module.css'
import CreateItemInput from '../profile_inputs/CreateItemInput';
import SaveBtnComponent from '../buttons/SaveBtnComponent';
import NotificationComponent from '../notifications/NotificationComponent';
import StaffSelect from '../select/StaffSelect';

import { createStaffItem, getEmployeePositions } from '../../api';


export default function CreateStaff() {
  const [staffData, setStaffData] = React.useState({
    "first_name": '',
    "last_name": '',
    "position": '',
    "comment": ''
  })
  const [employeePositionsData, setEmployeePositionsData] = React.useState([])
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const handleChange = (name, value) => {
    setStaffData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleSubbmit = async () => {
    console.log(staffData)
    const response = await createStaffItem(staffData)
    if (response.status === 201) {
      setTimeout(() => {
        setAlert({severity: 'success', message: 'Сотрудник создан'})
      }, 2500);
    } else {
      setTimeout(() => {
        setAlert({severity: 'error', message: 'Сотрудник не создан'})
      }, 3500);
    }
  }

  const employeePositions = async () => {
    const response = await getEmployeePositions()
    if (response.status === 200) {
      console.log(response.data)
      setEmployeePositionsData(response.data.positions)
    }
  }

  React.useEffect(() => {
    employeePositions()
  }, [])

  return(
    <div className={style.createBlock}>
      <div className={style.blockHeader}>
        <h3>Создать сотрудника</h3>
      </div>
      <NotificationComponent
      severity={alert.severity}
      message={alert.message}/>
      <div className={style.createItemData}>
        <div className={style.createItemBlock}>
          <div className={style.fieldName}>
            <h5>Имя Сотрудника</h5>
          </div>
          <CreateItemInput
          fieldType={'text'}
          fieldName={'first_name'}
          value={staffData.first_name}
          changeFunc={handleChange}
          />
        </div>
        <div className={style.createItemBlock}>
          <div className={style.fieldName}>
            <h5>Фамилия Сотрудника</h5>
          </div>
          <CreateItemInput
          fieldType={'text'}
          fieldName={'last_name'}
          value={staffData.last_name}
          changeFunc={handleChange}
          />
        </div>
        <div className={style.createItemBlock}>
          <div className={style.fieldName}>
            <h5>Должность Сотрудника</h5>
          </div>
          <StaffSelect
          dataList={employeePositionsData}
          changeFunc={handleChange}
          />
        </div>
        <div className={style.createItemBlock}>
          <div className={style.fieldName}>
            <h5>Комментарий</h5>
          </div>
          <CreateItemInput
          fieldType={'text'}
          fieldName={'comment'}
          value={staffData.comment}
          changeFunc={handleChange}
          />
        </div>
      </div>
      <SaveBtnComponent
      saveTitle={'Сотрудника'}
      clicked={handleSubbmit}
      />
    </div>
  );
}