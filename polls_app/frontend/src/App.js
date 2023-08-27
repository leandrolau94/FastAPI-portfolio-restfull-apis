import React from "react";
import { Container } from "@mui/material";
import Typography from '@mui/material/Typography';

import PollsList from "./components/PollsList";

function App() {
  return (
    <Container maxWidth="md">
      <Typography variant="h5" mt={2} mb={4} gutterBottom>
        Thanks for taking the time to do our survey
        and help us improve our services
      </Typography>
      <PollsList />
    </Container>
  );
}

export default App;
