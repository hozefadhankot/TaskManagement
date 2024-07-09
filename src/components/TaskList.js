import React from 'react';
import Task from './Task';
import { List } from '@mui/material';

const TaskList = ({ tasks, updateTaskStatus, deleteTask }) => {
    return (
        <List>
            {tasks.map((task) => (
                <Task
                    key={task.id}
                    task={task}
                    updateTaskStatus={updateTaskStatus}
                    deleteTask={deleteTask}
                />
            ))}
        </List>
    );
};

export default TaskList;
