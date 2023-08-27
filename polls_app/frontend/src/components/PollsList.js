import React, { useEffect, useState } from 'react';
import Question from './Question';
import api from './api';

const PollsList = () => {
  const [expanded, setExpanded] = useState('');

  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };

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
    <div>
        {
            questions.map(
                (question) => {
                    return(
                        <Question
                        key={question.id}
                        id={question.id}
                        question_text={question.question_text}
                        choices={question.choices}
                        expanded={expanded}
                        handleChange={handleChange} />
                    )
                }
            )
        }
    </div>
  );
}

export default PollsList;