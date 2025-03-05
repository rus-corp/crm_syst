import React from 'react';

import style from './create_expense.module.css'
import SelectDefComponent from '../select/SelectDefComponent';
import CreateItemInput from '../profile_inputs/CreateItemInput';
import SaveBtnComponent from '../buttons/SaveBtnComponent';
import NotificationComponent from '../notifications/NotificationComponent';

import { getCostItemsList, createExpenseItem } from '../../api';


export default function CreateExpense() {
  const [costItems, setCostItems] = React.useState([])
  const [expenseItem, setExpenseItem] = React.useState({
    category_id: '',
    amount: '',
    employee_id: null
  })
  const [alert, setAlert] =React.useState({severity: '', message: ''})

  const costItemsList = async () => {
    const response = await getCostItemsList()
    if (response.status === 200) {
      console.log(response.data)
      setCostItems(response.data)
    }
  }

  const handleChangeCostItem = (value) => {
    setExpenseItem((prevData) => ({
      ...prevData,
      category_id: value
    }))
  }

  const handleChangeAmount = (name, value) => {
    setExpenseItem((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleSubmit = () => {
    handleCreateExpenseItem(expenseItem)
  }

  React.useEffect(() => {
    costItemsList()
  }, [])

  const handleCreateExpenseItem = async (itemData) => {
    const response = await createExpenseItem(itemData)
    if (response.status === 201) {
      console.log(response)
      setAlert({severity: 'success', message: 'Расходы созданы'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
      }, 1500);
    } else if (response.status !== 201) {
      setAlert({severity: 'error', message: 'Расходы не созданы'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
      }, 2000);
    }
  }


  return(
    <div className={style.createBlock}>
      <div className={style.blockHeader}>
        <h3>Создать затрату</h3>
      </div>
      <div className={style.createBlockContent}>
        <SelectDefComponent
        dataTitle={'Статья'}
        dataList={costItems}
        changeFunc={handleChangeCostItem}
        />
        <CreateItemInput
        fieldType={'number'}
        fieldName={'amount'}
        value={expenseItem.amount}
        changeFunc={handleChangeAmount}
        />
      </div>
      <NotificationComponent
      severity={alert.severity}
      message={alert.message}
      />
      <SaveBtnComponent
      clicked={handleSubmit}/>
    </div>
  );
}