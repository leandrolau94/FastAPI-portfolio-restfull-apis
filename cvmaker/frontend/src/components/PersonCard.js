import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import Grid from '@mui/material/Unstable_Grid2';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import LocalPhoneIcon from '@mui/icons-material/LocalPhone';
import MarkEmailReadIcon from '@mui/icons-material/MarkEmailRead';
import LocationOnIcon from '@mui/icons-material/LocationOn';

const PersonCard = (props) => {

    const { id, full_name, email, address, postal_code, phone_number, work_experience, cv_skills, cv_projects, cv_languages } = props;

    return (
        <React.Fragment key={id}>
            <Box sx={{ width: "94%", height: "5%", mx: "auto", my: "0.5rem", border: "1px solid #b1afb3", borderRadius: "5px", padding: "5px", }}>
                <Typography variant="h6" gutterBottom>
                    {full_name}
                </Typography>
                <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
                    <Grid xs={6}>
                        <Stack direction="row" alignItems="center" gap={1}>
                            <LocalPhoneIcon />
                            <Typography variant='caption' display="block" gutterBottom>
                                {phone_number}
                            </Typography>
                        </Stack>
                    </Grid>
                    <Grid xs={6}>
                        <Stack direction="row" alignItems="center" gap={1}>
                            <MarkEmailReadIcon />
                            <Typography variant='caption' display="block" gutterBottom>
                                {email}
                            </Typography>
                        </Stack>
                    </Grid>
                    <Grid xs={6}>
                        <Stack direction="row" alignItems="center" gap={1}>
                            <LocationOnIcon />
                            <Typography variant='caption' display="block" gutterBottom>
                                {address}
                            </Typography>
                        </Stack>
                    </Grid>
                    <Grid xs={6}>
                        <Stack direction="row" alignItems="center" gap={1}>
                            <Typography variant='caption' display="block" gutterBottom>
                                postal code: {postal_code}
                            </Typography>
                        </Stack>
                    </Grid>
                    <Grid xs={12}>
                        <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center">
                            <ButtonGroup variant="contained" aria-label="outlined primary button group" sx={{ textAlign: "center" }}>
                                <Button>create cv</Button>
                                <Button>edit cv</Button>
                                <Button>delete cv</Button>
                            </ButtonGroup>
                        </Box>
                    </Grid>
                </Grid>
            </Box>
        </React.Fragment>
    )
};

export default PersonCard;