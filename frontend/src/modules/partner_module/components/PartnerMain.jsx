import React from 'react';

import style from '../styles/partners_main.module.css'
import { ComponentHeaderThreSwitch } from '../../../ui';

import PartnerExcursionComponent from './partials/PartnerExcursionComponent';
import PartnerTransferComponent from './partials/PartnerTransferComponent';
import PartnerOtherComponent from './partials/PartnerOtherComponent';

export default function PartnerMain() {
  const [selectedFilter, setSelectedFilter] = React.useState(0);
  const handleChangeFilterItem = (data) => {
    setSelectedFilter(data);
  }

  
  return(
    <div className={style.partnerBlock}>
      <ComponentHeaderThreSwitch
      componentName={'Партнеры'}
      btnName={'Партнера'}
      btnNavi={'create_partner'}
      handleChangeItem={handleChangeFilterItem}
      />
      <div className={style.partnerDataList}>
        {selectedFilter === 0 && <PartnerExcursionComponent />}
        {selectedFilter === 1 && <PartnerTransferComponent />}
        {selectedFilter === 2 && <PartnerOtherComponent />}
      </div>
    </div>
  );
}