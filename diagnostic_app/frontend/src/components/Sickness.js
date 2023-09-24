import React from 'react';

import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Tooltip from '@mui/material/Tooltip';

const Sickness = (props) => {

    const {id, name, symptoms, causes, treatment} = props;

  return (
    <Tooltip title={treatment} followCursor>
      <ListItem disablePadding>
        <ListItemButton>
          <ListItemText inset primary={name} />
        </ListItemButton>
      </ListItem>
    </Tooltip>
  )
}

export default Sickness;