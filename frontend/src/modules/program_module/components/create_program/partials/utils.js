export const groupedStaffExpenses = (staffExpensesData) => {
  const groupedByEmpl = {}

  staffExpensesData.forEach((element) => {
    const emp = element.employee
    const empId = emp.id

    if (!groupedByEmpl[empId]) {
      groupedByEmpl[empId] = {
        staffId: emp.id,
        staffName: emp.first_name,
        staffLastName: emp.last_name,
        staffPosition: emp.position,
        expenses: []
      }
    }

    groupedByEmpl[empId].expenses.push({
      category: element.category,
      price: element.amount
    })
  });
  return groupedByEmpl
}