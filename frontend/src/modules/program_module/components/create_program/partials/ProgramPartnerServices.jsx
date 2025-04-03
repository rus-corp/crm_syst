import React from 'react';

// import style from './'
import { getPartnerByIdWithServiceAndBank } from '../../../../../api';


export default function ProgramPartnerServices({ partnerId }) {
  const [partnerServices, setPartnerServices] = React.useState([])
  const getPartnerServices = async (partnerData) => {
    const response = await getPartnerByIdWithServiceAndBank(partnerData)
    if (response.status === 200) {
      console.log(response.data)
      setPartnerServices(response.data)
    }
  }

  React.useEffect(() => {
    getPartnerServices(partnerId)
  }, [partnerId])

  return(
    <>
    </>
  );
}