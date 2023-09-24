import React, { useState, useContext, useEffect } from 'react';
import { SicknessContext } from '../App';
import Sickness from './Sickness';

import TextField from '@mui/material/TextField';
import List from '@mui/material/List';
import Box from '@mui/material/Box';

const SicknessDashboard = () => {

    const sicknessContext = useContext(SicknessContext);

    const sickness = sicknessContext.sickness;

    const [searchVal, setSearchVal] = useState("");
    const [showDisease, setShowDisease] = useState(sickness);

    useEffect(() => {
        if (searchVal === "") {
            setShowDisease(sickness);
            return;
        };
    });

    const handleSymptomsLiveSearch = () => {
        if (searchVal === "") {
            setShowDisease(sickness);
            return;
        };
        const symptomsFilterBySearch = sickness.filter(
            item => item.symptoms.toLowerCase().includes(searchVal.toLowerCase())
        );
        setShowDisease(symptomsFilterBySearch);
    };

    useEffect(() => {
        handleSymptomsLiveSearch();
        // console.log(searchVal);
    }, [searchVal]);

  return (
    <Box>
        <TextField id="outlined-basic" label="Tap symptons to search possible diseases" variant="outlined" onChange={e => setSearchVal(e.target.value)} />
        <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
            {
                showDisease.map((showDisease) => {
                    return (
                        <Sickness key={showDisease.id} {...showDisease} />
                    )
                })
            }
        </List>
    </Box>
  )
};

export default SicknessDashboard;