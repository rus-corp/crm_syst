import React from 'react';
import { useSelector } from 'react-redux';

import { deleteClientFromProgramRoom } from '../../api';

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';


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

import CreateItemInput from '../profile_inputs/CreateItemInput';
import SaveBtnComponent from '../buttons/SaveBtnComponent';
import NotificationComponent from '../notifications/NotificationComponent';


export default function CheckOutModal({ programRoomId, visible, close }) {
  const clientProgram = useSelector((state) => state.program.clientProgram);
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const [checkOutData, setCheckOutData] = React.useState({
    program_room_id: programRoomId,
    program_client_id: clientProgram
  })
  const handleOutClient = async (clientData) => {
    const response = await deleteClientFromProgramRoom(clientData)
    if (response.status === 200) {
      setAlert({severity: 'access', message: 'Клиент выселен'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
        close(false)
      }, 2000);
    }
  }
  const handleSubbmit = () => {
    handleOutClient(checkOutData)
  } 
  
  const handleClose = () => close(false)

  return(
    <Modal
        open={visible}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
        >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Выселить клиента
            <NotificationComponent
            severity={alert.severity}
            message={alert.message}
            />
          </Typography>
          <Typography
          component={'div'}
          id="modal-modal-description"
          sx={{ mt: 2 }} style={{ marginBottom: '2rem'}}>
            {/* <CreateItemInput
            fieldTitle={'Дата заезда'}
            fieldType={'date'}
            changeFunc={handleChange}
            fieldName={'entry_date'}
            value={data.entry_date}
            /> */}
          </Typography>
          <SaveBtnComponent
          clicked={handleSubbmit}/>
        </Box>
      </Modal>
  );
}