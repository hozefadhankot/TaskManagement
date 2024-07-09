import React from 'react';
import { FormControl, InputLabel, Select, MenuItem, Box } from '@mui/material';

const TaskFilter = ({ statusFilter, setStatusFilter }) => {
    return (
        <Box my={2}>
            <FormControl fullWidth>
                <InputLabel>Status Filter</InputLabel>
                <Select
                    value={statusFilter}
                    onChange={(e) => setStatusFilter(e.target.value)}
                    label="Status Filter"
                >
                    <MenuItem value="All">All</MenuItem>
                    <MenuItem value="To Do">To Do</MenuItem>
                    <MenuItem value="In Progress">In Progress</MenuItem>
                    <MenuItem value="Done">Done</MenuItem>
                </Select>
            </FormControl>
        </Box>
    );
};

export default TaskFilter;
