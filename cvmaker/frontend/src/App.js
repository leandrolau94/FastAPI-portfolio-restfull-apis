import React, { useState, useEffect, createContext } from "react";
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import api from "./components/api";
import CreatePersonDashboard from "./components/CreatePersonDashboard";

export const PersonsContext = createContext();

const initialPersonState = {
  full_name: "",
  email: "",
  address: "",
  postal_code: 0,
  phone_number: "",
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <CreatePersonDashboard />
  },
  // {
  //   path: "/order",
  //   element: <OrderForTable />,
  // },
])

function App() {

  const [persons, setPersons] = useState([]);
  const [newPerson, setNewPerson] = useState(initialPersonState);

  const fetchPersons = async () => {
    return await api.get(
          "/persons/",
          {
              headers: {
                  'Access-Control-Allow-Origin': '*',
              },
              withCredentials: true,
          }
      ).then(response => {
          setPersons(response.data);
      }).catch(err => {
          console.log(err);
    });
  };

  useEffect(() => {
    fetchPersons();
  }, []);

  return (
    <PersonsContext.Provider value={{ persons: persons, setPersons: setPersons, fetchPersons: fetchPersons, newPerson: newPerson, setNewPerson: setNewPerson }}>
      <RouterProvider router={router}>
      </RouterProvider>
    </PersonsContext.Provider>
  );
}

export default App;
