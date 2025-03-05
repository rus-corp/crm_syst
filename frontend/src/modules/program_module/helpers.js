
export const handleClientCount = (clientList) => {
  let fullPaid = 0
  let avansPaid = 0
  let notPaid = 0
  for (const clientObj of clientList) {
    const clientStatus = clientObj.status
    if (clientStatus === "Full Payed") {
      fullPaid ++
    } else if (clientStatus === "Accepted") {
      avansPaid ++
    } else {
      notPaid ++
    }
  }
  return {PF: fullPaid, CF: avansPaid, NC: notPaid}
}

export const handleContractCount = (clientList) => {
  let count = 0
  for (let client of clientList) {
    if (client.contract_status == 'Signed') {
      count ++
    }
  }
  return count
}