import React, { useState, useEffect, useContext } from 'react';
import { OrderContext } from "../App";
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Unstable_Grid2';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

const FoodCard = (props) => {
    const {id, name, img_url, category, price} = props;

    const orderContext = useContext(OrderContext);
    const order = orderContext.order;
    const setOrder = orderContext.setOrder;

    const [quantity, setQuantity] = useState('');

    const handleQuantityChange = (event) => {
        setQuantity(event.target.value);
    };

    const handleAddToOrder = () => {
        console.log(order);
    };

    useEffect(() => {
        setOrder(previousState => {
            return {
                ...previousState,
                quantity: quantity,
            };
        });
    }, [quantity]);

  return (
    <Grid xs={4} sm={4} md={4} key={id}>
        <Card sx={{ maxWidth: 500 }}>
            <CardMedia
                sx={{ height: 140 }}
                image={img_url}
                title={name}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                {name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                {category} <strong>{price}</strong> &euro;
                </Typography>
            </CardContent>
            <CardActions>
                <FormControl sx={{ m: 1, minWidth: 80 }}>
                    <InputLabel id={`quantity-${id}`}>Quantity</InputLabel>
                    <Select
                    labelId={`quantity-${id}`}
                    id="quantity"
                    value={quantity}
                    onChange={handleQuantityChange}
                    autoWidth
                    label="Quantty"
                    >
                        <MenuItem value="">
                            <em>None</em>
                        </MenuItem>
                        <MenuItem value={1}>One</MenuItem>
                        <MenuItem value={2}>Two</MenuItem>
                        <MenuItem value={3}>Three</MenuItem>
                        <MenuItem value={4}>Four</MenuItem>
                        <MenuItem value={5}>Five</MenuItem>
                    </Select>
                </FormControl>
                <Button variant="contained" size="small" onClick={handleAddToOrder}>Add to order</Button>
            </CardActions>
        </Card>
    </Grid>
  )
}

export default FoodCard;