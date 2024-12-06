


export const formatedStatus = (status) => {
  if (status === "Accepted") {
    return 'Аванс Оплачен'
  } else if (status === "Full Payed") {
    return 'Полная оплата'
  } else {
    return 'Не оплачено'
  }
}

export const formatedContract = (contract) => {
  if (contract === 'SG') {
    return 'Подписан'
  } else if (contract === 'SD') {
    return 'Отправлен'
  } else {
    return 'Не отправлен'
  }
}


export const formatedClientStatus = (status) => {
  if (status === 'New') {
    return 'Новый'
  } else if (status === 'Regular') {
    return 'Постоянный'
  }
}