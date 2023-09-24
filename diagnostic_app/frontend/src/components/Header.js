import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import MedicalInformationIcon from '@mui/icons-material/MedicalInformation';

function Header() {
  
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <IconButton edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
            <MedicalInformationIcon />
          </IconButton>
          <Typography variant="h6" color="inherit" component="div">
            Wellcome to the Disease Diagnosis App
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
export default Header;