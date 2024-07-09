import React, { useState, useEffect } from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import TaskFilter from './components/TaskFilter';
import axios from 'axios';
import { Container, Typography, Box } from '@mui/material';
import './App.css';

const App = () => {
    const [tasks, setTasks] = useState([]);
    const [statusFilter, setStatusFilter] = useState('All');

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        try {
            const response = await axios.get('http://localhost:5000/tasks');
            console.log(response.data)
            setTasks(response.data);
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    };

    const addTask = async (task) => {
        try {
            const response = await axios.post('http://localhost:5000/tasks', task);
            setTasks([...tasks, response.data]);
        } catch (error) {
            console.error('Error adding task:', error);
        }
    };

    const updateTaskStatus = async (id, status) => {
        try {
            const response = await axios.put(`http://localhost:5000/tasks/${id}`, { status });
            setTasks(tasks.map(task => task.id === id ? response.data : task));
        } catch (error) {
            console.error('Error updating task status:', error);
        }
    };

    const deleteTask = async (id) => {
        try {
            await axios.delete(`http://localhost:5000/tasks/${id}`);
            setTasks(tasks.filter(task => task.id !== id));
        } catch (error) {
            console.error('Error deleting task:', error);
        }
    };

    const filteredTasks = tasks.filter(task => statusFilter === 'All' || task.status === statusFilter);

    return (
        <Container maxWidth="md">
            <Box my={4}>
                <Typography variant="h4" component="h1" gutterBottom>
                    Task Manager
                </Typography>
                <TaskForm addTask={addTask} />
                <TaskFilter statusFilter={statusFilter} setStatusFilter={setStatusFilter} />
                <TaskList tasks={filteredTasks} updateTaskStatus={updateTaskStatus} deleteTask={deleteTask} />
            </Box>
        </Container>
    );
};

export default App;
