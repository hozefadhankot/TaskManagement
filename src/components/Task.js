import React from 'react';
import { ListItem, ListItemText, Select, MenuItem, Button, Box } from '@mui/material';

const Task = ({ task, updateTaskStatus, deleteTask }) => {
    return (
        <ListItem>
            <ListItemText
                primary={task.title}
                secondary={task.description}
            />
            <Box>
                <Select
                    value={task.status}
                    onChange={(e) => updateTaskStatus(task.id, e.target.value)}
                    displayEmpty
                >
                    <MenuItem value="To Do">To Do</MenuItem>
                    <MenuItem value="In Progress">In Progress</MenuItem>
                    <MenuItem value="Done">Done</MenuItem>
                </Select>
            </Box>
            <Button onClick={() => deleteTask(task.id)} color="secondary">
                Delete
            </Button>
        </ListItem>
    );
};

export default Task;
