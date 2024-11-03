// frontend/src/App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [taskStatus, setTaskStatus] = useState(null);

  const triggerTask = async () => {
    const response = await axios.post("/run-task/", {
      task_name: "email_processing",
      task_data: { email: "user@example.com" }
    });
    setTaskStatus(response.data.status);
  };

  return (
    <div className="App">
      <h1>Business Automation Dashboard</h1>
      <button onClick={triggerTask}>Run Task</button>
      {taskStatus && <p>{taskStatus}</p>}
    </div>
  );
}

export default App;
