import React, { useState, useContext } from 'react';
import Grid from "@mui/material/Grid";
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import AddIcon from '@mui/icons-material/Add';
import Fab from '@mui/material/Fab';
import Snackbar from '@mui/material/Snackbar';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';

import { EmployeeContext } from '../App';

const EmployeeForm = () => {

    const employeeContext = useContext(EmployeeContext);

    const employee = employeeContext.employee;
    const setEmployee = employeeContext.setEmployee;
    const postNewEmployee = employeeContext.postNewEmployee;
    const fetchAllEmployees = employeeContext.fetchAllEmployees;

    const [postDanger, setPostDanger] = useState("");
    const [open, setOpen] = useState(false);

    const handleClick = () => {
        setOpen(true);
    };
    
    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
          return;
        };
    
        setOpen(false);
    };

    const action = (
        <React.Fragment>
          <IconButton
            size="small"
            aria-label="close"
            color="inherit"
            onClick={handleClose}
          >
            <CloseIcon fontSize="small" />
          </IconButton>
        </React.Fragment>
    );

    const handleClearAllInputs = () => {
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("age").value = "";
        document.getElementById("genre").value = "";
        document.getElementById("country").value = "";
        document.getElementById("role").value = "";
        document.getElementById("wage").value = "";
    };

    const handlePostNewEmployee = async () => {
        if (employee.full_name === "" || employee.email === "" || employee.age === "" || employee.genre === "" || employee.country === "" || employee.role === "" || employee.wage === "") {
            setPostDanger("There is at least one empty field. Please fill out the missing information");
            handleClick();
        } else {
            await postNewEmployee();
            setEmployee(
                {
                    ...employee,
                    full_name: "",
                    email: "",
                    age: 0,
                    genre: "",
                    country: "",
                    role: "",
                    wage: 0.0,
                }
            );
            handleClearAllInputs();
            return await fetchAllEmployees();
        };
    };

    return (
        <>
            <Box sx={{ maxHeight: '45vh', maxWidth: "90vw", m: 1, textAlign: "center", }}>
                <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
                    <Grid item xs={6}>
                        <TextField fullWidth label="full name" id="name" onChange={(e) => {setEmployee({...employee, full_name: e.target.value})}} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="email" id="email" onChange={(e) => {setEmployee({...employee, email: e.target.value})}} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="age" id="age" onChange={(e) => {setEmployee({...employee, age: parseInt(e.target.value)})}} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="genre" id="genre" onChange={(e) => {setEmployee({...employee, genre: e.target.value})}} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="country" id="country" onChange={(e) => {setEmployee({...employee, country: e.target.value})}} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="role" id="role" onChange={(e) => {setEmployee({...employee, role: e.target.value})}} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="wage per year" id="wage" onChange={(e) => {setEmployee({...employee, wage: parseFloat(e.target.value)})}} />
                    </Grid>
                    <Grid item xs={6}>
                        <Fab size='medium' color="primary" aria-label="add" onClick={handlePostNewEmployee}>
                            <AddIcon />
                        </Fab>
                        <Snackbar
                            open={open}
                            autoHideDuration={6000}
                            onClose={handleClose}
                            message={postDanger}
                            action={action}
                        />
                    </Grid>
                </Grid>
            </Box>
        </>
    )
}

export default EmployeeForm;