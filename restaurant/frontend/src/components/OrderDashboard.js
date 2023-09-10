import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Unstable_Grid2';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import api from './api';
import FoodCard from './FoodCard';

const OrderDashboard = () => {
  
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
    <Box sx={{ flexGrow: 1, padding: 2 }}>
      <FormControl sx={{ m: 4, color: "white", textAlign: "center" }}>
        <FormLabel id="demo-row-radio-buttons-group-table" sx={{ color: "white" }}>Select your table number</FormLabel>
        <RadioGroup
          row
          aria-labelledby="demo-row-radio-buttons-group-table"
          name="row-radio-buttons-group"
        >
          {
            tables.map((table, index) => {
              return (
                <FormControlLabel value={`${table.id}`} control={<Radio />} label={`Table ${table.table_number}`} />
              )
            })
          }
        </RadioGroup>
      </FormControl>
      <Grid container spacing={{ xs: 4, md: 8 }} columns={{ xs: 4, sm: 8, md: 12 }}>
        {
          foods.map((foods) => {
            return (
              <FoodCard key={foods.id} {...foods} />
            )
          })
        }
      </Grid>
    </Box>
  )
};

export default OrderDashboard;