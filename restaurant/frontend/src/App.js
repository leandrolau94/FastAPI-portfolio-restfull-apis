import React from "react";
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import OrderDashboard from "./components/OrderDashboard";

function App() {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="md">
        <Box sx={{ bgcolor: '#cfe8fc', height: '100vh' }}>
          <OrderDashboard />
        </Box>
      </Container>
    </React.Fragment>
  );
}

export default App;
