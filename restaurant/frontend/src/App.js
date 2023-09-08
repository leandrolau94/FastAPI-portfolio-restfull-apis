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
        <Box sx={{ bgcolor: '#1b283b', height: '100vh', overflow: "scroll" }}>
          <OrderDashboard />
        </Box>
      </Container>
    </React.Fragment>
  );
}

export default App;
