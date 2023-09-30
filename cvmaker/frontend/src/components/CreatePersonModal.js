import React, { useContext } from 'react';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import Button from '@mui/material/Button';
import NoteAddRoundedIcon from '@mui/icons-material/NoteAddRounded';

import { PersonsContext } from '../App';
import api from './api';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: "90%",
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
    justifyContext: "center",
    textAlign: "center",
    '& .MuiTextField-root': { m: 1, width: '25ch' },
};

const CreatePersonModal = ({open, handleClose}) => {

    const personsContext = useContext(PersonsContext);
    const newPerson = personsContext.newPerson;
    const setNewPerson = personsContext.setNewPerson;
    const fetchPersons = personsContext.fetchPersons;

    const handlePostNewPerson = async () => {
        await api.post(
            "/persons/",
            newPerson,
            {
                headers: {
                    'Access-Control-Allow-Origin': '*',
                },
                withCredentials: true,
            }
        ).then(response => {
            console.log(response);
        }).catch(err => {
            console.log(err);
        });
        await fetchPersons();
        return handleClose();
    };

    return (
        <Modal aria-labelledby="transition-modal-title" aria-describedby="transition-modal-description" open={open} onClose={handleClose} closeAfterTransition slots={{ backdrop: Backdrop }} slotProps={{ backdrop: {timeout: 500,},}}>
            <Fade in={open}>
                <Box component="form" sx={style} noValidate autoComplete='off'>
                    <div>
                        <TextField
                        id="outlined-multiline-flexible"
                        label="Full Name"
                        onChange={(e) => {setNewPerson({...newPerson, full_name: e.target.value})}}
                        multiline
                        maxRows={4}
                        />
                        <TextField
                        id="outlined-multiline-flexible"
                        label="Email"
                        onChange={(e) => {setNewPerson({...newPerson, email: e.target.value})}}
                        multiline
                        maxRows={4}
                        />
                        <TextField
                        id="outlined-multiline-flexible"
                        label="Address"
                        onChange={(e) => {setNewPerson({...newPerson, address: e.target.value})}}
                        multiline
                        maxRows={4}
                        />
                        <TextField
                        id="outlined-multiline-flexible"
                        label="Postal Code"
                        onChange={(e) => {setNewPerson({...newPerson, postal_code: parseInt(e.target.value)})}}
                        multiline
                        maxRows={4}
                        />
                        <TextField
                        id="outlined-multiline-flexible"
                        label="Phone Number"
                        onChange={(e) => {setNewPerson({...newPerson, phone_number: e.target.value})}}
                        multiline
                        maxRows={4}
                        />
                        <Button variant="contained" endIcon={<NoteAddRoundedIcon />} onClick={handlePostNewPerson}>
                            Create
                        </Button>
                    </div>
                </Box>
            </Fade>
        </Modal>
    );
};

export default CreatePersonModal;