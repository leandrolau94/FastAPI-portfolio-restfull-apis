import React, { useContext } from 'react';
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
import ListSubheader from '@mui/material/ListSubheader';
import IconButton from '@mui/material/IconButton';
import EuroIcon from '@mui/icons-material/Euro';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';
import { Link } from 'react-router-dom';
import { OrderContext } from '../App';

const OrderForTable = () => {

    const orderContext = useContext(OrderContext);

    const order = orderContext.order;

    const tables = orderContext.tables;

    const foods = orderContext.foods;

    const table = tables.find((obj) => {
        return obj.id === order.table_id;
    });

    const itemData = [];

    const tableOrderArr = table.table_orders;

    tableOrderArr.forEach(element => {
        var ordered_food = foods.find(food => {
            return food.id === element.food_id;
        });
        itemData.push({
            img: ordered_food.img_url,
            title: ordered_food.name,
            quantity: `${element.quantity}`,
            price: ordered_food.price,
            rows: 2,
            cols: 2,
            featured: true,
        });
    });

    if (tableOrderArr.length === 0) {
        return (
            <React.Fragment>
                <Stack sx={{ width: '100%' }} spacing={2}>
                    <Alert variant="outlined" severity="info">
                        You have not ordered yet. Please, come back and make your order
                    </Alert>
                </Stack>
                <Box sx={{ p: 2, textAlign: "center", maxHeight: '5vh' }}>
                    <Link to="/">Back to order</Link>
                </Box>
            </React.Fragment>
        )
    }

    return (
        <React.Fragment>
            <ImageList sx={{ maxWidth: '80vw', maxHeight: '70vh', mx: 'auto' }}>
                <ImageListItem key="Subheader" cols={2}>
                    <ListSubheader component="div">Your Order</ListSubheader>
                </ImageListItem>
                {itemData.map((item) => (
                    <ImageListItem key={item.img}>
                    <img
                        src={`${item.img}?w=248&fit=crop&auto=format`}
                        srcSet={`${item.img}?w=248&fit=crop&auto=format&dpr=2 2x`}
                        alt={item.title}
                        title={item.title}
                        loading="lazy"
                    />
                    <ImageListItemBar
                        title={item.title}
                        subtitle={`quantity: ${item.quantity}`}
                        actionIcon={
                        <IconButton
                            sx={{ color: 'rgba(255, 255, 255, 0.54)' }}
                            aria-label={`info about ${item.title}`}
                        >
                            {item.price}
                            <EuroIcon />
                        </IconButton>
                        }
                    />
                    </ImageListItem>
                ))}
            </ImageList>
            <Box sx={{ p: 2, textAlign: "center", maxHeight: '5vh' }}>
                <Link to="/">Back to order</Link>
            </Box>
        </React.Fragment>
    )
}

export default OrderForTable;