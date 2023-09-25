import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import MedicalInformationIcon from '@mui/icons-material/MedicalInformation';

function Header() {
  
  return (
    <Box sx={{ display: "flex", width: "100%", margin: 0 }}>
      <AppBar position="static">
        <Toolbar variant="regular" sx={{ backgroundColor: "#17283b" }}>
          <IconButton edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
            <MedicalInformationIcon />
          </IconButton>
          <Typography variant="h6" color="inherit" component="div">
            Aplicacion de Diagnostico de Enfermedades
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
export default Header;