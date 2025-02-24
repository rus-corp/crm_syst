import React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';


export default function StaffSelect({ dataList, changeFunc }) {
  const [selectedData, setSelectedData] = React.useState('')
  const handleChange = (ev) => {
    console.log(ev.target.value)
    setSelectedData(ev.target.value)
    changeFunc('position', ev.target.value)
  }
  return(
    <FormControl sx={{ m: 1, minWidth: '100%',}} size="small">
      <InputLabel id="demo-simple-select-label">Должность</InputLabel>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={selectedData}
        label="Должность"
        onChange={handleChange}
      >
        {dataList.map((dataItem, indx) => (
          <MenuItem key={indx}
          value={dataItem}>{dataItem}</MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}