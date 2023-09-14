import React, { useState, useContext } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionDetails from '@mui/material/AccordionDetails';
import AccordionSummary from '@mui/material/AccordionSummary';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import AddIcon from '@mui/icons-material/Add';
import Fab from '@mui/material/Fab';

import { EmployeeContext } from '../App';

const EmployeeForm = () => {

    const [expanded, setExpanded] = useState(false);

    const handleChange = (panel) => (event, isExpanded) => {
        setExpanded(isExpanded ? panel : false);
    };

    const employeeContext = useContext(EmployeeContext);

    const employee = employeeContext.employee;
    const setEmployee = employeeContext.setEmployee;
    const postNewEmployee = employeeContext.postNewEmployee;
    const fetchAllEmployees = employeeContext.fetchAllEmployees;

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

    return (
        <>
            <Box sx={{ maxHeight: '30vh', m: 1, textAlign: "center", overflowY: "scroll" }}>
                <Accordion expanded={expanded === 'panel1'} onChange={handleChange('panel1')}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel1bh-content"
                    id="panel1bh-header"
                    >
                        <Typography sx={{ width: '33%', flexShrink: 0 }}>
                            Full Name
                        </Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <TextField fullWidth label="tap full name" id="name" onChange={(e) => {setEmployee({...employee, full_name: e.target.value})}} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel2'} onChange={handleChange('panel2')}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel2bh-content"
                    id="panel2bh-header"
                    >
                        <Typography sx={{ width: '33%', flexShrink: 0 }}>Email</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <TextField fullWidth label="tap email" id="email" onChange={(e) => {setEmployee({...employee, email: e.target.value})}} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel3'} onChange={handleChange('panel3')}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel3bh-content"
                    id="panel3bh-header"
                    >
                        <Typography sx={{ width: '33%', flexShrink: 0 }}>
                            Age
                        </Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <TextField fullWidth label="tap age" id="age" onChange={(e) => {setEmployee({...employee, age: parseInt(e.target.value)})}} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel4'} onChange={handleChange('panel4')}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel4bh-content"
                    id="panel4bh-header"
                    >
                        <Typography sx={{ width: '33%', flexShrink: 0 }}>Genre</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <TextField fullWidth label="tap genre" id="genre" onChange={(e) => {setEmployee({...employee, genre: e.target.value})}} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel5'} onChange={handleChange('panel5')}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel5bh-content"
                    id="panel5bh-header"
                    >
                        <Typography sx={{ width: '33%', flexShrink: 0 }}>Country</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <TextField fullWidth label="tap country" id="country" onChange={(e) => {setEmployee({...employee, country: e.target.value})}} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel6'} onChange={handleChange('panel6')}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel6bh-content"
                    id="panel6bh-header"
                    >
                        <Typography sx={{ width: '33%', flexShrink: 0 }}>Role</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <TextField fullWidth label="tap role" id="role" onChange={(e) => {setEmployee({...employee, role: e.target.value})}} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
                <Accordion expanded={expanded === 'panel7'} onChange={handleChange('panel7')}>
                    <AccordionSummary
                    expandIcon={<ExpandMoreIcon />}
                    aria-controls="panel7bh-content"
                    id="panel7bh-header"
                    >
                        <Typography sx={{ width: '33%', flexShrink: 0 }}>Wage per year</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <TextField fullWidth label="tap wage per year" id="wage" onChange={(e) => {setEmployee({...employee, wage: parseFloat(e.target.value)})}} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
            </Box>
            <Box sx={{ height: '7vh', textAlign: "center", m: 1 }}>
                <Fab color="primary" aria-label="add" onClick={handlePostNewEmployee}>
                    <AddIcon />
                </Fab>
            </Box>
        </>
    )
}

export default EmployeeForm;