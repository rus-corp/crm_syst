import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';


import CreateItemInput from '../profile_inputs/CreateItemInput';
import SaveBtnComponent from '../buttons/SaveBtnComponent';
import NotificationComponent from '../notifications/NotificationComponent';
import { createCostItem } from '../../api';

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

export default function ModalComponent({ visible, close }) {
  const [open, setOpen] = React.useState(visible);
  const [title, setTitle] = React.useState({
    title: ''
  })
  const [alert, setAlert] = React.useState({severity: '', message: ''})
  const handleOpen = () => setOpen(true);
  const handleClose = () => {
    setOpen(false)
    close(false)
  };
  const handleChange = (name, value) => {
    setTitle({[name]: value})
  }

  const createNewItem = async (itemData) => {
    const response = await createCostItem(itemData)
    if (response.status === 201) {
      setAlert({severity: 'success', message: 'Статья создана'})
      setTimeout(() => {
        setAlert({severity: '', message: ''})
        setOpen(false)
      }, 2000);
    } else if (response.status !== 201) {
      setAlert({severity: 'error', message: 'Статья не создана'})
    }
  }

  const handleSubbmit = () => {
    createNewItem(title)
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
            Создать Статью
            <NotificationComponent
            severity={alert.severity}
            message={alert.message}
            />
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }} style={{ marginBottom: '2rem'}}>
            Название Статьи:
            <CreateItemInput
            fieldName={'title'}
            fieldType={'text'}
            value={title.title}
            changeFunc={handleChange}
            />
          </Typography>
          <SaveBtnComponent
          clicked={handleSubbmit}/>
        </Box>
      </Modal>
    </div>
  );
}