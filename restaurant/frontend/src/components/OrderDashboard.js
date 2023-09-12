import React, { useState, useEffect, useContext } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Unstable_Grid2';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import { styled } from '@mui/material/styles';
import FoodCard from './FoodCard';
import { Link } from 'react-router-dom';

import { OrderContext } from '../App';

const BpIcon = styled('span')(({ theme }) => ({
  borderRadius: '50%',
  width: 16,
  height: 16,
  boxShadow:
    theme.palette.mode === 'dark'
      ? '0 0 0 1px rgb(16 22 26 / 40%)'
      : 'inset 0 0 0 1px rgba(16,22,26,.2), inset 0 -1px 0 rgba(16,22,26,.1)',
  backgroundColor: theme.palette.mode === 'dark' ? '#394b59' : '#f5f8fa',
  backgroundImage:
    theme.palette.mode === 'dark'
      ? 'linear-gradient(180deg,hsla(0,0%,100%,.05),hsla(0,0%,100%,0))'
      : 'linear-gradient(180deg,hsla(0,0%,100%,.8),hsla(0,0%,100%,0))',
  '.Mui-focusVisible &': {
    outline: '2px auto rgba(19,124,189,.6)',
    outlineOffset: 2,
  },
  'input:hover ~ &': {
    backgroundColor: theme.palette.mode === 'dark' ? '#30404d' : '#ebf1f5',
  },
  'input:disabled ~ &': {
    boxShadow: 'none',
    background:
      theme.palette.mode === 'dark' ? 'rgba(57,75,89,.5)' : 'rgba(206,217,224,.5)',
  },
}));

const BpCheckedIcon = styled(BpIcon)({
  backgroundColor: '#137cbd',
  backgroundImage: 'linear-gradient(180deg,hsla(0,0%,100%,.1),hsla(0,0%,100%,0))',
  '&:before': {
    display: 'block',
    width: 16,
    height: 16,
    backgroundImage: 'radial-gradient(#fff,#fff 28%,transparent 32%)',
    content: '""',
  },
  'input:hover ~ &': {
    backgroundColor: '#106ba3',
  },
});

// Inspired by blueprintjs
function BpRadio(props) {
  return (
    <Radio
      disableRipple
      color="default"
      checkedIcon={<BpCheckedIcon />}
      icon={<BpIcon />}
      {...props}
    />
  );
}

const StyledLink = styled(Link)`
  margin: auto;
  padding: 7px 15px;
  font-family: sans-serif;
  font-size: 1rem;
  font-weight: 300;
  text-decoration: none;
  color: white;
  background-color: #2979ff;
  border-radius: 5px;
`;

const OrderDashboard = () => {

  const [tableID, setTableID] = useState('');

  const orderContext = useContext(OrderContext);
  
  // const order = orderContext.order;
  const setOrder = orderContext.setOrder;

  const foods = orderContext.foods;
  // const setFoods = orderContext.setFoods;

  const tables = orderContext.tables;
  // const setTables = orderContext.setTables;

  const handleTableChange = (event) => {
    setTableID(event.target.value);
  };

  useEffect(() => {
    setOrder(previousState => {
      return {
        ...previousState,
        table_id: parseInt(tableID),
      };
    });
  }, [tableID]);

  return (
    <React.Fragment>
      <FormControl sx={{ m: 2, color: "black", textAlign: "center", bgcolor: "#f57c00", padding: 2, borderRadius: "5px", overflow: "scroll", maxHeight: '20vh' }}>
        <FormLabel id="demo-row-radio-buttons-group-table" sx={{ color: "black" }}>Select your table number</FormLabel>
        <RadioGroup
          row
          aria-labelledby="demo-row-radio-buttons-group-table"
          name="row-radio-buttons-group"
          value={tableID}
          onChange={handleTableChange}
          sx={{ textAlign: "center" }}
        >
          {
            tables.map((table, index) => {
              return (
                <FormControlLabel key={`${table.id}`} value={`${table.id}`} control={<BpRadio />} label={`Table ${table.table_number}`} />
              )
            })
          }
        </RadioGroup>
      </FormControl>
      <Box sx={{ p: 2, bgcolor: '#1b283b', maxHeight: '60vh', borderRadius: "5px", overflow: "scroll" }}>
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
          {
            foods.map((foods) => {
              return (
                <FoodCard key={foods.id} {...foods} />
              )
            })
          }
        </Grid>
      </Box>
      <Box sx={{ p: 2, textAlign: "center", maxHeight: '5vh' }}>
        <StyledLink to="/order">See order</StyledLink>
      </Box>
    </React.Fragment>
  )
};

export default OrderDashboard;