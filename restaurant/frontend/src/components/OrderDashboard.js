import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Unstable_Grid2';
import api from './api';
import FoodCard from './FoodCard';

const OrderDashboard = () => {
  
  const [foods, setFoods] = useState([])

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

  useEffect(() => {
    fetchFoods();
  }, []);

  return (
    <Box sx={{ flexGrow: 1 }}>
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
  )
};

export default OrderDashboard;