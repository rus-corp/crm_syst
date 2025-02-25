import React from 'react';

import style from './create_expense.module.css'
import SelectDefComponent from '../select/SelectDefComponent';
import CreateItemInput from '../profile_inputs/CreateItemInput';
import SaveBtnComponent from '../buttons/SaveBtnComponent';

import { getCostItemsList } from '../../api';


export default function CreateExpense() {
  const [costItems, setCostItems] = React.useState([])

  const costItemsList = async () => {
    const response = await getCostItemsList()
    if (response.status === 200) {
      console.log(response.data)
      setCostItems(response.data)
    }
  }

  const handleChangeCostItem = (event) => {
    console.log(event)
  }

  React.useEffect(() => {
    costItemsList()
  }, [])


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
        <CreateItemInput />
      </div>
      <SaveBtnComponent />
    </div>
  );
}