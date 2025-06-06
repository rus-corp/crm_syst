import React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';


export default function EmployeeSelect({ dataList, changeFunc }) {
  const [selectedData, setSelectedData] = React.useState('')
  
  const handleChange = (ev) => {
    console.log(ev.target.value)
    setSelectedData(ev.target.value)
    changeFunc(ev.target.value)
  }

  return(
    <FormControl sx={{ m: 1, minWidth: '100%',}} size="small">
      <InputLabel id="demo-simple-select-label">Сотрудник</InputLabel>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        label='Сотрудник'
        value={selectedData}
        onChange={handleChange}
      >
        {dataList.map((dataItem) => (
          <MenuItem key={dataItem.id}
          value={dataItem.id}>{dataItem.first_name} {dataItem.last_name}</MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}