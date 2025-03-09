import React from 'react';

import style from '../../styles/partner_partials.module.css'
import { getPartnersFilterList } from '../../../../api';

export default function PartnerOtherComponent() {
  const [partnerList, setPartnerList] = React.useState([]);
  const getPartnerList = async () => {
    const response = await getPartnersFilterList('Остальное');
    if (response.status === 200) {
      console.log(response.data);
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
        partnerName={partner.title}
        partnerLawName={partner.law_title}
        partnerPrice={partner.price}
        partnerServiceName={partner.service_name}
        />
      ))}
    </div>
  );
}