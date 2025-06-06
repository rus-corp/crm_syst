


export const formatedStatus = (status) => {
  if (status === "Accepted") {
    return 'Аванс Оплачен'
  } else if (status === "Full Payed") {
    return 'Полная оплата'
  } else {
    return 'Не подтверждено'
  }
}

export const formatedContract = (contract) => {
  if (contract === 'Signed') {
    return 'Подписан'
  } else if (contract === 'Sended') {
    return 'Отправлен'
  } else {
    return 'Не отправлен'
  }
}


export const formatedClientStatus = (status) => {
  if (status === 'New' || status === undefined) {
    return 'Новый'
  } else if (status === 'Regular') {
    return 'Постоянный'
  }
  else {
    return ''
  }
}