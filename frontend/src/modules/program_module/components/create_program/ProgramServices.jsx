import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import style from '../styles/create_program.module.css'
import { SaveBtnComponent, SmallButton, NotificationComponent, ProfileInput } from '../../../../ui';
import ProgramPartnerItem from './partials/ProgramPartnerItem';
import { getPartnersFilterList, appendPartnerRoProgramReq, createProgramPrices } from '../../../../api';


export default function ProgramServices() {
  const location = useLocation()
  const navigation = useNavigate()
  const { programId, programTitle, nights } = location.state
  const [partnerList, setPartnerList] = React.useState([])
  const [programPartner, setProgramPartner] = React.useState([])
  const [alert, setAlert] = React.useState({'severity': '', 'message': ''})
  const handleCreateProgramPartner = async (partnerData) => {
    const response = await appendPartnerRoProgramReq(partnerData)
    if (response.status === 201) {
      setAlert({severity: 'success', message: 'Партнер добавлен в программу'})
      setTimeout(() => {
        setAlert({severity:'', message:''})
        navigation('/create_program/total_program', {
          state: {
            programId: programId,
            programTitle: programTitle,
            nights: nights
          }
        })
      }, 2000);
    }
  }
  const handleCreateProgramPrices = async (programData) => {
    const response = await createProgramPrices(programData)
      // setAlert({severity: 'success', message: 'Партнер добавлен в программу'})
      // setTimeout(() => {
      //   setAlert({severity:'', message:''})
      //   navigation('/create_program/total_program', {
      //     state: {
      //       programId: programId,
      //       programTitle: programTitle,
      //       nights: nights
      //     }
      //   })
      // }, 2000);
    // }
  }
  const getPartnersList = async() => {
    const response = await getPartnersFilterList()
    if (response.status === 200) {
      setPartnerList(response.data)
    }
  }

  const appendServiceToProgram = (partnerId, serviceId, state) => {
    if (state) {
      setProgramPartner((prevData) => (
        [
          ...prevData,
          {
            program_id: programId,
            partner_id: partnerId,
            service_id: serviceId
          }
        ]
      ))
    } else if (!state) {
      setProgramPartner((prevData) => (
        prevData.filter((item) => item.service_id !== serviceId)
      ))
    }
  }
  const handleSubmit = () => {
    handleCreateProgramPartner(programPartner)
    handleCreateProgramPrices(programId)
  }

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
                    handleAppendServiceToProgram={appendServiceToProgram}
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