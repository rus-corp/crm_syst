import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import Checkbox from '@mui/material/Checkbox';
import { useSelector } from 'react-redux';

import { appendClientToProgramRoom } from '../../api';

import CreateItemInput from '../profile_inputs/CreateItemInput';
import SaveBtnComponent from '../buttons/SaveBtnComponent';
import NotificationComponent from '../notifications/NotificationComponent';


const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

export default function CheckInModal({ visible, close, programRoomId, dataFunc }) {
  const programStartDate = useSelector((state) => state.program.programStartDate);
  const programEndDate = useSelector((state) => state.program.programEndDate);
  const clientProgram = useSelector((state) => state.program.clientProgram);
  const [open, setOpen] = React.useState(visible);
  const [data, setData] = React.useState({
    program_client_id: clientProgram,
    program_room_id: programRoomId,
    entry_date: programStartDate,
    departue_date: programEndDate,
    comment: null,
    no_sharing: false
  })
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const handleClose = () => {
    setOpen(false)
    close(false)
  };
  const handleChange = (name, value) => {
    setData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handlePopulateClient = async (clientData) => {
    const response = await appendClientToProgramRoom(clientData)
    if (response.status === 201) {
      setAlert({severity: 'success', message: 'Клиент Заселен'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
        handleClose()
      }, 2000);
    }
  }

  const handleChangeSharing = (event) => {
    const newState = event.target.checked;
    setData((prevData) => ({
      ...prevData,
      no_sharing: newState
    }))
  }
  // dataFunc if false -> заселяем клиента if true -> выселяем
  const handleSubbmit = () => {
    console.log(data)
    handlePopulateClient(data)
  }

  return (
    <div>
      <Modal
        open={visible}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
        >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Заселить клиента
            <NotificationComponent
            severity={alert.severity}
            message={alert.message}
            />
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }} style={{ marginBottom: '2rem'}}>
            <CreateItemInput
            fieldTitle={'Дата заезда'}
            fieldType={'date'}
            changeFunc={handleChange}
            fieldName={'entry_date'}
            value={data.entry_date}
            />
            <CreateItemInput
            fieldTitle={'Дата выезда'}
            fieldType={'date'}
            changeFunc={handleChange}
            fieldName={'departue_date'}
            value={data.departue_date}
            />
            <CreateItemInput
            fieldTitle={'Комментарий'}
            fieldType={'text'}
            changeFunc={handleChange}
            fieldName={'comment'}
            value={data.comment}
            />
            <span>Запретить подселение</span>
            <Checkbox onChange={handleChangeSharing}/>
          </Typography>
          <SaveBtnComponent
          clicked={handleSubbmit}/>
        </Box>
      </Modal>
    </div>
  );
}