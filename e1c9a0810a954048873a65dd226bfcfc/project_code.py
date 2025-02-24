javascript// Backend Code (Node.js with Express and MongoDB)

// Import necessary packages
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

// Initialize the app
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Connect to MongoDB
mongoose.connect('mongodb://localhost/task-management', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

// Task Schema
const TaskSchema = new mongoose.Schema({
  title: String,
  description: String,
  priority: String,
  deadline: Date,
  completed: Boolean
});

// Task Model
const Task = mongoose.model('Task', TaskSchema);

// API Endpoints
app.get('/api/tasks', async (req, res) => {
  try {
    const tasks = await Task.find();
    res.json(tasks);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

app.post('/api/tasks', async (req, res) => {
  const task = new Task({
    title: req.body.title,
    description: req.body.description,
    priority: req.body.priority,
    deadline: req.body.deadline,
    completed: req.body.completed
  });

  try {
    const newTask = await task.save();
    res.status(201).json(newTask);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.put('/api/tasks/:id', async (req, res) => {
  try {
    const updatedTask = await Task.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(updatedTask);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

app.delete('/api/tasks/:id', async (req, res) => {
  try {
    const deletedTask = await Task.findByIdAndRemove(req.params.id);
    res.json(deletedTask);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

// Frontend Code (React.js)

// TaskList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TaskList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/tasks')
      .then(response => setTasks(response.data))
      .catch(error => console.error('Error fetching tasks:', error));
  }, []);

  return (
    <ul>
      {tasks.map(task => (
        <li key={task._id}>{task.title}</li>
      ))}
    </ul>
  );
}

export default TaskList;

// TaskForm.js
import React, { useState } from 'react';
import axios from 'axios';

function TaskForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [priority, setPriority] = useState('');
  const [deadline, setDeadline] = useState('');
  const [completed, setCompleted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newTask = { title, description, priority, deadline, completed };
    try {
      await axios.post('http://localhost:5000/api/tasks', newTask);
      setTitle('');
      setDescription('');
      setPriority('');
      setDeadline('');
      setCompleted(false);
    } catch (error) {
      console.error('Error creating task:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={title} onChange={e => setTitle(e.target.value)} placeholder="Title" />
      <input type="text" value={description} onChange={e => setDescription(e.target.value)} placeholder="Description" />
      <input type="text" value={priority} onChange={e => setPriority(e.target.value)} placeholder="Priority" />
      <input type="date" value={deadline} onChange={e => setDeadline(e.target.value)} />
      <input type="checkbox" checked={completed} onChange={e => setCompleted(e.target.checked)} />
      <button type="submit">Add Task</button>
    </form>
  );
}

export default TaskForm;

// TaskItem.js
import React from 'react';
import axios from 'axios';

function TaskItem({ task }) {
  const handleDelete = async () => {
    try {
      await axios.delete(`http://localhost:5000/api/tasks/${task._id}`);
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  return (
    <div>
      <h3>{task.title}</h3>
      <p>{task.description}</p>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
}

export default TaskItem;

// App.js
import React from 'react';
import TaskList from './TaskList';
import TaskForm from './TaskForm';

function App() {
  return (
    <div>
      <h1>Task Management App</h1>
      <TaskForm />
      <TaskList />
    </div>
  );
}

export default App;
