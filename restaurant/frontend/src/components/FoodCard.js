import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Unstable_Grid2';

const FoodCard = (props) => {
    const {id, name, category, price} = props;
  return (
    <Grid xs={2} sm={4} md={4} key={id}>
        <Card sx={{ maxWidth: 345 }}>
            <CardMedia
                sx={{ height: 140 }}
                image="https://www.juventudrebelde.cu/images/medias/2019/02/yUw2AU_07-02-2019_13.02.11.000000.jpg"
                title={`${name}`}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                {name}  {price}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                {category}
                </Typography>
            </CardContent>
            <CardActions>
                {/* <Button size="small">Share</Button> */}
                <Button size="small">Order</Button>
            </CardActions>
        </Card>
    </Grid>
  )
}

export default FoodCard;