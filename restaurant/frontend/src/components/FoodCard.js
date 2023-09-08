import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Unstable_Grid2';

const FoodCard = (props) => {
    const {id, name, img_url, category, price} = props;
  return (
    <Grid xs={2} sm={4} md={4} key={id}>
        <Card sx={{ maxWidth: 345 }}>
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
                {/* <Button size="small">Share</Button> */}
                <Button variant="contained" size="small">Add to order</Button>
            </CardActions>
        </Card>
    </Grid>
  )
}

export default FoodCard;