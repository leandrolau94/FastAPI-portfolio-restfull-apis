import React from 'react';
import { styled } from '@mui/material/styles';
import MuiAccordion from '@mui/material/Accordion';
import ArrowForwardIosSharpIcon from '@mui/icons-material/ArrowForwardIosSharp';
import MuiAccordionSummary from '@mui/material/AccordionSummary';
import MuiAccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import Choices from './Choices';

const Accordion = styled((props) => (
    <MuiAccordion disableGutters elevation={0} square {...props} />
  ))(({ theme }) => ({
    border: `1px solid ${theme.palette.divider}`,
    '&:not(:last-child)': {
      borderBottom: 0,
    },
    '&:before': {
      display: 'none',
    },
  }));
  
  const AccordionSummary = styled((props) => (
    <MuiAccordionSummary
      expandIcon={<ArrowForwardIosSharpIcon sx={{ fontSize: '0.9rem' }} />}
      {...props}
    />
  ))(({ theme }) => ({
    backgroundColor:
      theme.palette.mode === 'dark'
        ? 'rgba(255, 255, 255, .05)'
        : 'rgba(0, 0, 0, .03)',
    flexDirection: 'row-reverse',
    '& .MuiAccordionSummary-expandIconWrapper.Mui-expanded': {
      transform: 'rotate(90deg)',
    },
    '& .MuiAccordionSummary-content': {
      marginLeft: theme.spacing(1),
    },
  }));
  
  const AccordionDetails = styled(MuiAccordionDetails)(({ theme }) => ({
    padding: theme.spacing(2),
    borderTop: '1px solid rgba(0, 0, 0, .125)',
  }));

const Question = (props) => {
    const {id, question_text, choices, expanded, handleChange} = props;
  return (
    <Accordion expanded={expanded === `panel${id}`} onChange={handleChange(`panel${id}`)}>
        <AccordionSummary aria-controls={`panel${id}d-content`} id={`panel${id}d-header`}>
          <Typography>{question_text}</Typography>
        </AccordionSummary>
        <AccordionDetails>
            <Choices
            choicesArray={choices}
            polls_question_id={id} />
        </AccordionDetails>
    </Accordion>
  )
}

export default Question;