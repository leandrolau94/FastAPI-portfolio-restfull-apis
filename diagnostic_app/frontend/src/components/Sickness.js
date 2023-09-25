import React from 'react';

import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import SicknessDetail from './SicknessDetail';

const Sickness = (props) => {

    const {id, name, symptoms, causes, treatment} = props;

  return (
    <ListItem disablePadding sx={{ textAlign: "center", justifyContent: "center" }}>
      <ListItemText inset primary={
        <SicknessDetail id={id} name={name} symptoms={symptoms} causes={causes} treatment={treatment} />
      } sx={{ textAlign: "center", justifyContent: "center" }} />
    </ListItem>
  )
}

export default Sickness;