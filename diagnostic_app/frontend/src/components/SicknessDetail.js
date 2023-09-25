import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: "90%",
    height: "60%",
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
    overflow: "scroll",
};

const SicknessDetail = ({id, name, symptoms, causes, treatment}) => {

    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return (
        <Box sx={{ justifyContent: "center", textAlign: "center", width: "90%", "&:hover": { backgroundColor: "#17283b", borderRadius: "5px" } }}>
            <Button id={`btn-modal-${id}`} onClick={handleOpen} sx={{ width: "100%", height: "100%", "&:hover": { color: "#ffffff" } }}>{name}</Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby={`modal-modal-title-${id}`}
                aria-describedby={`modal-modal-description-${id}`}
            >
                <Box sx={style}>
                <Typography id={`modal-modal-title-${id}`} variant="h3" component="h2">
                    {name}
                </Typography>
                <Typography id={`modal-modal-description-${id}`} sx={{ mt: 2 }}>
                    <Typography variant='h5' sx={{ color: "#451d6e" }}>
                        Sintomas:
                    </Typography>
                    {symptoms}
                </Typography>
                <Typography id={`modal-modal-description-${id}`} sx={{ mt: 2 }}>
                    <Typography variant='h5' sx={{ color: "#96115a" }}>
                        Causas:
                    </Typography>
                    {causes}
                </Typography>
                <Typography id={`modal-modal-description-${id}`} sx={{ mt: 2 }}>
                    <Typography variant='h5' sx={{ color: "#318745" }}>
                        Tratamiento:
                    </Typography>
                    {treatment}
                </Typography>
                </Box>
            </Modal>
        </Box>
    )
};

export default SicknessDetail;