import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import style from '../styles/create_program.module.css'
import { SaveBtnComponent, SmallButton, NotificationComponent, ProfileInput } from '../../../../ui';
import ProgramPartnerItem from './partials/ProgramPartnerItem';
import { getPartnersFilterList } from '../../../../api';


export default function ProgramServices() {
  const location = useLocation()
  const navigation = useNavigate()
  const { programId, programTitle, nights } = location.state
  const [partnerList, setPartnerList] = React.useState([])
  const [alert, setAlert] = React.useState({'severity': '', 'message': ''})
  const getPartnersList = async() => {
    const response = await getPartnersFilterList()
    if (response.status === 200) {
      console.log(response.data)
      setPartnerList(response.data)
    }
  }
  const addComponent = () => {}
  const handleSubmit = () => {}
  React.useEffect(() => {
    getPartnersList()
  }, [])
  return(
    <section className={style.createProgram}>
          <div className={style.createProgramData}>
            <div className={style.sectionHeader}>
              <h2>Дополнительные услуги {programTitle}</h2>
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
                fieldData='15'
                fieldTitle='Количество человек'
                />
              </div>
            </div>
            <aside className={style.sectionCreateData}>
              <div className={style.dataHeader}>
                <h4>Добавить услуги</h4>
              </div>
              <div className={style.sectionAppendHotels}>
                <div className={style.hotelList}>
                  {partnerList.map((partnerItem) => (
                    <ProgramPartnerItem key={partnerItem.id}
                    partnerId={partnerItem.id}
                    partnerTitle={partnerItem.title}
                    partnerCategory={partnerItem.category}
                    />
                  ))}
                </div>
              </div>
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