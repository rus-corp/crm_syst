import React from 'react';

import style from '../../styles/partner_partials.module.css'
import { getPartnersFilterList } from '../../../../api';
import PartnerItem from './PartnerItem';


export default function PartnerExcursionComponent() {
  const [partnerList, setPartnerList] = React.useState([]);
  const getPartnerList = async () => {
    const response = await getPartnersFilterList('Экскурсии');
    if (response.status === 200) {
      setPartnerList(response.data);
    }
  }
  
  React.useEffect(() => {
    getPartnerList();
  }, [])

  return(
    <div className={style.partnerDataList}>
      {partnerList.map((partner) => (
        <PartnerItem key={partner.id}
        partnerId={partner.id}
        partnerName={partner.title}
        partnerLawName={partner.law_title}
        partnerServices={partner.partner_services}
        />
      ))}
    </div>
  );
}