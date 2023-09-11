import React, { createContext, useState } from "react";
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import OrderDashboard from "./components/OrderDashboard";

export const OrderContext = createContext();

const initialOrderState = {
  quantity: 0,
  delivered: false,
  order_time: new Date().toJSON(),
  food_id: 1,
  table_id: 1,
};

function App() {

  const [order, setOrder] = useState(initialOrderState);

  return (
    <OrderContext.Provider value={{order: order, setOrder: setOrder}}>
      <React.Fragment>
        <CssBaseline />
        <Container maxWidth="lg">
          <Box sx={{ height: '100vh' }}>
            <OrderDashboard />
          </Box>
        </Container>
      </React.Fragment>
    </OrderContext.Provider>
  );
}

export default App;
