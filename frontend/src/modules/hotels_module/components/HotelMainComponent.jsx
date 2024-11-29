import React from 'react';
import { hotels } from '../../../data_test/hotels';

import style from './hotels.module.css'
import { ComponentHeader } from '../../../ui';
import HotelListComponent from './hotels_list/HotelListComponent';
import HotelCardComponent from './hotels_cards/HotelCardComponent';


export default function HotelMainComponent() {
  const [hotelsData, setHotelsData] = React.useState([])
  const [hotelOption, setHotelOption] = React.useState(true)

  function handleChangeOption(data) {
    setHotelOption(data)
  }

  React.useEffect(() => {
    setHotelsData(hotels)
  }, [hotels])

  return(
    <div className={style.hotelsComponent}>
      <ComponentHeader
      componentName='Отели'
      componentDataCount={hotelsData.length}
      componentSetData={handleChangeOption}
      />
      {hotelOption ? <HotelListComponent hotelsList={hotelsData}/> : <HotelCardComponent hotelsList={hotelsData}/>}
    </div>
  );
}