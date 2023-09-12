import React, { createContext, useState, useEffect } from "react";
import api from "./components/api";
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import OrderDashboard from "./components/OrderDashboard";
import OrderForTable from "./components/OrderForTable";
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: "/",
    element: <React.Fragment>
              <CssBaseline />
              <Container maxWidth="lg">
                <Box sx={{ height: '100vh' }}>
                  <OrderDashboard />
                </Box>
              </Container>
            </React.Fragment>
  },
  {
    path: "/order",
    element: <OrderForTable />,
  },
])

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
  const [foods, setFoods] = useState([]);
  const [tables, setTables] = useState([]);

  const fetchFoods = async () => {
    return await api.get(
      "/food/?skip=0&limit=1000",
      {
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
        withCredentials: true,
      }
    ).then(response => {
      setFoods(response.data);
    }).catch(err => {
      console.log(err);
    })
  };

  const fetchTables = async () => {
    return await api.get(
      "/table/?skip=0&limit=100",
      {
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
        withCredentials: true,
      }
    ).then(response => {
      setTables(response.data);
    }).catch(err => {
      console.log(err);
    });
  };

  useEffect(() => {
    fetchFoods();
    fetchTables();
  }, []);

  return (
    <OrderContext.Provider value={{order: order, setOrder: setOrder, foods: foods, setFoods: setFoods, tables: tables, setTables: setTables}}>
      <RouterProvider router={router}>
      </RouterProvider>
    </OrderContext.Provider>
  );
}

export default App;
