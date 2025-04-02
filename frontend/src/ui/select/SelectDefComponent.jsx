import React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';


import ModalComponent from '../modal/ModalComponent';


export default function SelectDefComponent({ dataTitle, dataList, changeFunc }) {
  const [open, setOpen] = React.useState(false)
  const [selectedData, setSelectedData] = React.useState('')
  
  
  const handleChange = (ev) => {
    setSelectedData(ev.target.value)
    changeFunc(ev.target.value)
  }

  const handleClose = () => {
    setOpen(false)
  }
  
  return(
    <FormControl sx={{ m: 1, minWidth: '100%',}} size="small">
      <InputLabel id="demo-simple-select-label">{dataTitle}</InputLabel>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={selectedData}
        label={dataTitle}
        onChange={handleChange}
      >
        {dataList?.map((dataItem) => (
          <MenuItem key={dataItem.id}
          value={dataItem.id}>{dataItem.title}</MenuItem>
        ))}
        <MenuItem onClick={() => setOpen(true)} value=''>Создать статью</MenuItem>
      </Select>
      <ModalComponent
      visible={open}
      close={handleClose}/>
    </FormControl>
  );
}