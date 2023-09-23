import React, { useState, useEffect, createContext } from "react";
import { Container } from "@mui/material";
import Typography from '@mui/material/Typography';

import PollsList from "./components/PollsList";
import api from "./components/api";
import Header from "./components/Header";

export const QuestionsContext = createContext(null);

function App() {

  const [questions, setQuestions] = useState([]);

  const fetchQuestions = async () => {
    return await api.get(
          "/questions/?skip=0&limit=100",
          {
              headers: {
                  'Access-Control-Allow-Origin': '*',
              },
              withCredentials: true,
          }
      ).then(response => {
          setQuestions(response.data);
      }).catch(err => {
          console.log(err);
    });
  };

  useEffect(() => {
    fetchQuestions();
  }, []);

  return (
    <QuestionsContext.Provider value={{ questions: questions, setQuestions: setQuestions, fetchQuestions: fetchQuestions }}>
      <Header />
      <Container maxWidth="md" sx={{ marginTop: 4 }}>
        <PollsList />
      </Container>
    </QuestionsContext.Provider>
  );
}

export default App;
