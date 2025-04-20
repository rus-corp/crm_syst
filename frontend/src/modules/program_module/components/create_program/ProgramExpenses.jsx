import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import style from '../styles/create_program.module.css'
import { NotificationComponent, CreateItemInput, SaveBtnComponent, ProfileInput, SmallButton } from '@/ui';
import ProgramEmployeeItemCreate from './partials/ProgramEmployeeItemCreate';
import ProgramStaticExpense from './partials/ProgramStaticExpense';
import ProgramPartnerseExpense from './partials/ProgramPartnersExpense';
import { getStaffs } from '@/api';
import { createProgramExpenses } from '../../../../api';


const staticCategories = ['Затраты на организацию', 'Реклама', 'Маржа', 'Мерчь']

const staticCategoriesMap = {
  'Затраты на организацию': 'organization',
  'Реклама': 'marketing',
  'Маржа': 'margin',
  'Мерчь': 'merch'
}



export default function ProgramExpenses() {
  const location = useLocation()
  const navigation = useNavigate()
  const { programId, programTitle, nights, clientCount } = location.state
  const [alert, setAlert] = React.useState({severity:'', message:''})
  const [staffExpenseItem, setStaffExpenseItem] = React.useState([{
    'program_id': programId,
    'employee_id': null,
    'expenses': []
  }])
  const [staticExpense, setStaticExpense] = React.useState(
    staticCategories.map((category) => ({category: staticCategoriesMap[category], 'amount': 0, program_id: programId, 'expense_type': 'client'}))
  )

  const [staffData, setStaffData] = React.useState([])
  
  const appendProgramExpenses = async (expenseData) => {
    const response = await createProgramExpenses(expenseData)
    if (response.status === 201) {
      setAlert({'severity': 'success', message: 'Затраты добавлены'})
      setTimeout(() => {
        setAlert({severity:'', message:''})
        navigation('/create_program/add_partners', {
          state: {
            programId: programId,
            programTitle: programTitle,
            nights: nights
          }
        })
      }, 2000);
    }
  }
  
  const handleChangeExpense = (indx, name, value) => {
    setStaffExpenseItem((prevData) => 
      prevData.map((item, ind) => 
      ind === indx ? 
        {
          ...item,
          expenses: item.expenses.some((expense) => expense.category === name)
            ? item.expenses.map((expense) => 
              expense.category === name
                ? {...expense, amount: value} : expense
              ) : 
              [...item.expenses, {category: name, amount: value}]
        } : item))
  }
  
  const handleChangeEmpl = (indx, value) => {
    setStaffExpenseItem(
      (prevData) => 
        prevData.map((item, ind) => 
        ind === indx ? {...item, employee_id: value} : item)
    )
  }
  
  const handleSubmit = () => {
    const payload = {
      'static_expense': staticExpense,
      'employee_expense': staffExpenseItem
    }
    appendProgramExpenses(payload)
  }

  const addComponent = () => {
    setStaffExpenseItem((prevData) => ([
      ...prevData,
      {
        program_id: programId,
        employee_id: '',
        expenses: []
      }
    ]))
  }
  
  const getStaffData = async () => {
    const response = await getStaffs()
    if (response.status === 200) {
      setStaffData(response.data)
    }
  }

  const handleChangeStaticExpense = (indx, name, value) => {
    const newData = [...staticExpense]
    newData[indx].amount = value
    setStaticExpense(newData)
  }

  React.useEffect(() => {
    getStaffData()
  }, [])

  return(
    <section className={style.createProgram}>
      <div className={style.createProgramData}>
        <div className={style.sectionHeader}>
          <h2>Затраты на программу {programTitle}</h2>
          <NotificationComponent
          severity={alert.severity}
          message={alert.message}
          />
        </div>
        <div className={style.expenseHeader}>
          <div className={style.programStaticData}>
            <ProfileInput
            fieldData={nights}
            fieldTitle='Количество ночей'
            />
          </div>
          <div className={style.programStaticData}>
            <ProfileInput
            fieldData={clientCount}
            fieldTitle='Количество человек'
            />
          </div>
        </div>
        <aside className={style.sectionCreateData}>
          <div className={style.dataHeader}>
            <h4>Затраты на сотрудников</h4>
          </div>
          <div className={style.orgExpense}>
            <div className={style.expenseItemHeader}>
              <p>Сотрудник</p>
              <p>Проезд</p>
              <p>Питание</p>
              <p>ЗП</p>
              <p>Проживание</p>
            </div>
            <div className={style.expenseStaff}>
              {staffExpenseItem.map((item, indx) => (
                <ProgramEmployeeItemCreate key={indx}
                staffData={staffData}
                indx={indx}
                handleChangeEmpl={handleChangeEmpl}
                handleChangeExpense={handleChangeExpense}
                />
              ))}
            </div>
            <SmallButton
            btnData={'Добавить сотрудника'}
            handleClick={addComponent}
            />
          </div>
        </aside>
        <aside className={style.staticExpenseBlock}>
          <div className={style.dataHeader}>
            <h4>Статические затраты</h4>
          </div>
          {staticExpense.map((categoryItem, indx) => (
            <ProgramStaticExpense key={indx}
            indx={indx}
            expenseTitle={categoryItem.category}
            fieldName={staticCategoriesMap[categoryItem.category]}
            expenseValue={categoryItem.amount}
            handleChange={handleChangeStaticExpense}
            />
          ))}
        </aside>

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