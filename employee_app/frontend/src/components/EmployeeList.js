import React, { useContext } from 'react';
import Alert from '@mui/material/Alert';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';

import { EmployeeContext } from '../App';

const EmployeeList = () => {

    const employeeContext = useContext(EmployeeContext);

    const allEmployees = employeeContext.allEmployees;

    const columns = [
        { field: 'id', headerName: 'ID', width: 90 },
        {
          field: 'full_name',
          headerName: 'Full Name',
          width: 200,
          editable: true,
        },
        {
          field: 'email',
          headerName: 'Email',
          width: 200,
          editable: true,
        },
        {
          field: 'age',
          headerName: 'Age',
          type: 'number',
          width: 110,
          editable: true,
        },
        {
          field: 'genre',
          headerName: 'Genre',
          width: 160,
          editable: true,
        },
        {
            field: 'country',
            headerName: 'Country',
            width: 160,
            editable: true,
        },
        {
            field: 'role',
            headerName: 'Role',
            width: 160,
            editable: true,
        },
        {
            field: 'wage',
            headerName: 'Wage',
            type: 'number',
            width: 160,
            editable: true,
        },
        {
            field: 'start_date',
            headerName: 'Date Started',
            width: 200,
            editable: true,
        },
    ];
      
    const rows = allEmployees;

    if (allEmployees.length === 0) {
        return (
            <Alert severity="success" color="info" sx={{ m: 5 }}>
                Not employees found. Please add one to start.
            </Alert>
        )
    }

    return (
        <Box sx={{ maxHeight: '15vh', maxWidth: '96vh', m: 3 }}>
            <DataGrid
                rows={rows}
                columns={columns}
                initialState={{
                pagination: {
                    paginationModel: {
                    pageSize: 5,
                    },
                },
                }}
                pageSizeOptions={[5]}
                checkboxSelection
                disableRowSelectionOnClick
            />
        </Box>
    )
}

export default EmployeeList;