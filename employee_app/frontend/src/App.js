import React, { createContext, useState, useEffect } from "react";
import api from "./components/api";
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";

import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: "/",
    element: <React.Fragment>
              <CssBaseline />
              <Container maxWidth="lg">
                <Box sx={{ maxHeight: '100vh' }}>
                  <EmployeeForm />
                  <EmployeeList />
                </Box>
              </Container>
            </React.Fragment>
  },
  // {
  //   path: "/employee/:id",
  //   element: <OrderForTable />,
  // },
])

export const EmployeeContext = createContext();

const initialEmployeeState = {
  full_name: "",
  email: "",
  age: 0,
  genre: "",
  country: "",
  role: "",
  wage: 0.0,
  start_date: new Date().toJSON(),
};

function App() {

  const [employee, setEmployee] = useState(initialEmployeeState);
  const [allEmployees, setAllEmployees] = useState([]);

  const fetchAllEmployees = async () => {
    return await api.get(
      "/employees/",
      {
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
        withCredentials: true,
      }
    ).then(response => {
      setAllEmployees(response.data);
    }).catch(err => {
      console.log(err);
    })
  };

  const postNewEmployee = async () => {
    return await api.post(
      "/employees/",
      employee,
      {
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
        withCredentials: true,
      }
    ).then(response => {
      console.log(`Employee successfully created`);
    }).catch(err => {
      console.log(err);
    })
  };

  useEffect(() => {
    fetchAllEmployees();
  }, []);

  return (
    <EmployeeContext.Provider value={{
      employee: employee,
      setEmployee: setEmployee,
      allEmployees: allEmployees,
      setAllEmployees: setAllEmployees,
      fetchAllEmployees: fetchAllEmployees,
      postNewEmployee: postNewEmployee,
    }}>
      <RouterProvider router={router}>
      </RouterProvider>
    </EmployeeContext.Provider>
  );
}

export default App;
