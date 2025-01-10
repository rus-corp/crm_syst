import React from 'react';

import style from './hotels.module.css'
import { ComponentHeader } from '../../../ui';
import HotelListComponent from './hotels_list/HotelListComponent';
import HotelCardComponent from './hotels_cards/HotelCardComponent';

import { getHotels } from '../../../api';


export default function HotelMainComponent() {
  const [hotelsData, setHotelsData] = React.useState([])
  const [hotelOption, setHotelOption] = React.useState(true)

  const getHotelsData = async () => {
    const response = await getHotels()
    if (response.status === 200) {
      setHotelsData(response.data)
    }
  }
  function handleChangeOption(data) {
    setHotelOption(data)
  }

  React.useEffect(() => {
    getHotelsData()
  }, [])

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