import React, { useState, useEffect, createContext } from "react";
import { Container } from "@mui/material";

import api from "./components/api";
import Header from "./components/Header";
import SicknessDashboard from "./components/SicknessDashboard";

export const SicknessContext = createContext();

function App() {

  const [sickness, setSickness] = useState([]);

  const fetchSickness = async () => {
    return await api.get(
          "/sickness/diagnostic",
          {
              headers: {
                  'Access-Control-Allow-Origin': '*',
              },
              withCredentials: true,
          }
      ).then(response => {
          setSickness(response.data);
      }).catch(err => {
          console.log(err);
    });
  };

  useEffect(() => {
    fetchSickness();
  }, []);

  return (
    <SicknessContext.Provider value={{ sickness: sickness, setSickness: setSickness, fetchSickness: fetchSickness }}>
      <Header />
      <Container maxWidth="md" sx={{ marginTop: 4, display: "flex", justifyContent: "center", padding: "5px", maxWidth: "90%", maxHeight: "80%" }}>
        <SicknessDashboard />
      </Container>
    </SicknessContext.Provider>
  );
}

export default App;
