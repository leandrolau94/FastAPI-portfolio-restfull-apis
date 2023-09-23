import React, { useState, useContext } from 'react';
import Question from './Question';
import { QuestionsContext } from '../App';

const PollsList = () => {
  const [expanded, setExpanded] = useState('');

  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };

  const questionsContext = useContext(QuestionsContext);

  const questions = questionsContext.questions;

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