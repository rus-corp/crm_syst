import React from 'react';

import style from './styles/hotelsList.module.css'

import { getProgramHotels } from '../../../api';

export default function HotelsListComponent({ programSlug }) {
  const [programHotels, setProgramHotels] = React.useState(hotelList)

  const handleGetProgramHotels = async(slug) => {
    const response = await getProgramHotels(slug)
    if (response.status === 200) {
      setProgramHotels(response.data.hotels)
    }
  }

  React.useEffect(() => {
    if (programSlug) {
      handleGetProgramHotels(programSlug)
    }
  }, [programSlug])
  return(
    <>
      <div className={style.activeHotels}>
        <div className={style.activeHotelsHeader}>
          <h4>Проживание Программы</h4>
        </div>
        <div className={style.hotelsList}>
          {programHotels.map((hotelItem) => (
            <HotelItem key={hotelItem.id}
            hotelTitle={hotelItem.title}
            roomVolume={hotelItem.room_volumes}
            />
          ))}
        </div>
      </div>
    </>
  );
}


function HotelItem({ hotelTitle, roomVolume }) {
  return (
    <div className={style.hotelItem}>
      <div className={style.hotelItemData}>
        <p>Название</p>
        <h5>{hotelTitle}</h5>
      </div>
      <div className={style.hotelItemData}>
        <p>Номера</p>
        <h6>{roomVolume}</h6>
      </div>
      <div className={style.hotelItemData}>
        <p>Места</p>
        <h6>{roomVolume}</h6>
      </div>
    </div>
  );
}


const activeHotels = [
  {
    "id": 1,
    "title": "Отель Казан Султан",
    "address": "улица Зайни Султана, д.12",
    "contacts": "555-44-88",
    "desc": "В погоне за впечатлениями важно возвращаться туда, где можно хорошо отдохнуть. Отель «Отель Казан Султан» находится в Казани. Этот отель располагается неподалёку от центра города. Рядом с отелем можно прогуляться. Неподалёку: Миллениум Парк, Музей социалистического быта и Площадь Габдуллы Тукая.",
    "city": "Архыз",
    "email": "sultan@mail.ru",
    "room_volumes": 12
  }
]

const hotelList = [
  {
    "id": 1,
    "title": "Отель Казан Султан",
    "address": "улица Зайни Султана, д.12",
    "contacts": "555-44-88",
    "desc": "В погоне за впечатлениями важно возвращаться туда, где можно хорошо отдохнуть. Отель «Отель Казан Султан» находится в Казани. Этот отель располагается неподалёку от центра города. Рядом с отелем можно прогуляться. Неподалёку: Миллениум Парк, Музей социалистического быта и Площадь Габдуллы Тукая.",
    "city": "Архыз",
    "email": "sultan@mail.ru",
    "room_volumes": 12
  },
  {
    "id": 2,
    "title": "Отель Gizzat Plaza",
    "address": "улица Тази Гиззата, д.16",
    "contacts": "555-63-96",
    "desc": "Удачный вариант для активного туриста! Отель «Отель Gizzat Plaza» располагается в Казани. Этот отель находится неподалёку от центра города. Рядом с отелем — Петропавловский собор, Кремлёвская и Музей социалистического быта.",
    "city": "Архыз",
    "email": "gizzat@mail.ru",
    "room_volumes": 16
  },
  {
    "id": 3,
    "title": "Апарт-отель Кунак",
    "address": "Каюма Насыри, 13",
    "contacts": "555-77-85",
    "desc": "Апарт-отель Кунак» расположен в Казани. Отель расположен в историческом центре города",
    "city": "Архыз",
    "email": "kunak@mail.ru",
    "room_volumes": 11
  },
  {
    "id": 4,
    "title": "Отель Измайлово Бета",
    "address": "Измайловское шоссе, 71, корпус 2Б",
    "contacts": "777-96-84",
    "desc": "Доступный трехвездочный бизнес-отель в зеленом районе города, входит в гостиничный комплекс «Измайлово». Расположен недалеко от метро «Партизанская», станции МЦК «Измайлово» и Измайловского парка – одного из самых больших в Москве.",
    "city": "Мурманск",
    "email": "beta@mail.ru",
    "room_volumes": 11
  },
  {
    "id": 5,
    "title": "Отель Измайлово Гамма",
    "address": "Измайловское шоссе, д.71, корп. 4Г-Д",
    "contacts": "777-84-21",
    "desc": "Отель «Гамма Измайлово» является частью легендарного гостиничного комплекса на 2000 номеров в районе Измайлово, в 600 м от большого парка. До метро «Партизанская» ― 6 минут ходьбы, до метро «Измайлово» ― 7 минут. За 15 минут на транспорте можно добраться до центра Москвы.",
    "city": "Мурманск",
    "email": "gamma@mail.ru",
    "room_volumes": 12
  },
  {
    "id": 6,
    "title": "Отель Movenpiсk",
    "address": "улица Земляной Вал, д.70",
    "contacts": "777-95-65",
    "desc": "Скоротать вечер или приятно провести время перед сном в уютной атмосфере можно в баре. Для гостей работает ресторан. Хотите оставаться на связи? В отеле есть бесплатный Wi-Fi. Для путешественников на машине организована платная парковка.",
    "city": "Москва",
    "email": "movenpick@mail.ru",
    "room_volumes": 11
  }
]