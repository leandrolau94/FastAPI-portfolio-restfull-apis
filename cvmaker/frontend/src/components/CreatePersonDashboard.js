import React, { useState, useEffect, useContext } from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Paper from '@mui/material/Paper';
import Fab from '@mui/material/Fab';
import List from '@mui/material/List';
import MenuIcon from '@mui/icons-material/Menu';
import AddIcon from '@mui/icons-material/Add';
import SearchIcon from '@mui/icons-material/Search';
import MoreIcon from '@mui/icons-material/MoreVert';

import CreatePersonModal from './CreatePersonModal';
import { PersonsContext } from '../App';
import PersonCard from './PersonCard';

const StyledFab = styled(Fab)({
    position: 'absolute',
    zIndex: 1,
    top: -30,
    left: 0,
    right: 0,
    margin: '0 auto',
});

const CreatePersonDashboard = () => {

    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const personsContext = useContext(PersonsContext);
    const persons = personsContext.persons;
      
    return (
      <div>
        <React.Fragment>
            <CssBaseline />
            <Paper square sx={{ pb: '50px' }}>
                <Typography variant="h5" gutterBottom component="div" sx={{ p: 2, pb: 0 }}>
                People List
                </Typography>
                <List sx={{ mb: 2 }}>
                {
                    persons.map((persons) => {
                        return (
                            <PersonCard key={persons.id} {...persons} />
                        );
                    })
                }
                </List>
            </Paper>
            <AppBar position="fixed" color="primary" sx={{ top: 'auto', bottom: 0 }}>
                <Toolbar>
                <IconButton color="inherit" aria-label="open drawer">
                    <MenuIcon />
                </IconButton>
                <StyledFab color="secondary" aria-label="add" onClick={handleOpen}>
                    <AddIcon />
                </StyledFab>
                <CreatePersonModal open={open} handleClose={handleClose} />
                <Box sx={{ flexGrow: 1 }} />
                <IconButton color="inherit">
                    <SearchIcon />
                </IconButton>
                <IconButton color="inherit">
                    <MoreIcon />
                </IconButton>
                </Toolbar>
            </AppBar>
        </React.Fragment>
      </div>
    );
};

export default CreatePersonDashboard;