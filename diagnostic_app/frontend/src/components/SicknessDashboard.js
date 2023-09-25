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
    <Box sx={{ textAlign: "center", justifyContent: 'center', width: "100%", height: "100%" }}>
        <TextField id="outlined-basic" label="Teclee los sintomas para mostrar posibles enfermedades" variant="outlined" onChange={e => setSearchVal(e.target.value)} sx={{ width: "100%", marginBottom: 3 }} />
        <List sx={{ width: '100%', bgcolor: 'background.paper', textAlign: "center", justifyContent: 'center', mx: "auto", borderLeft: "1px solid gray", borderTop: "1px solid gray", borderBottom: "1px solid gray", borderRadius: "5px", overflowY: "scroll" }}>
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