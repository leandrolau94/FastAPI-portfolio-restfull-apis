import React, { useState, useContext } from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormHelperText from '@mui/material/FormHelperText';
import FormLabel from '@mui/material/FormLabel';
import Button from '@mui/material/Button';

import { QuestionsContext } from '../App';
import api from './api';

const Choices = (props) => {
    const { choicesArray, polls_question_id } = props

    const [value, setValue] = useState('');
    const [error, setError] = useState(false);
    const [helperText, setHelperText] = useState('Choose wisely');

    const handleRadioChange = (event) => {
        setValue(event.target.value);
        setHelperText(' ');
        setError(false);
    };

    const questionsContext = useContext(QuestionsContext);

    const fetchQuestions = questionsContext.fetchQuestions;

    const incrementVotesCount = async () => {
        return await api.put(
            `/questions/${polls_question_id}/choices/${value}`,
            {
                headers: {
                    'Access-Control-Allow-Origin': '*',
                },
                withCredentials: true,
            }
        )
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (value !== '') {
        setHelperText(`You have chosen, thanks`);
        setError(false);
        } else {
        setHelperText('Please select a choice.');
        setError(true);
        };
        await incrementVotesCount();
        await fetchQuestions();
        console.log("votes attribute successfully incremented.");
    };

    return (
        <form onSubmit={handleSubmit}>
        <FormControl sx={{ m: 3 }} error={error} variant="standard">
            <FormLabel id={`demo-error-radios`}>Available Choices</FormLabel>
            <RadioGroup
            row
            aria-labelledby={`demo-error-radios`}
            name="quiz"
            value={value}
            onChange={handleRadioChange}
            >
                {
                    choicesArray.map(
                        (choice) => {
                            return (
                                <FormControlLabel key={choice.id} value={choice.id} control={<Radio />} label={`${choice.choice_text}(${choice.votes_number})`} />
                            )
                        }
                    )
                }
            </RadioGroup>
            <FormHelperText>{helperText}</FormHelperText>
            <Button sx={{ mt: 1, mr: 1 }} type="submit" variant="outlined">
                Submit Choice
            </Button>
        </FormControl>
        </form>
    );
}

export default Choices;