#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error(new Error('Usage: ./6-completed_tasks.js <API_URL>'));
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Parse the response body to JSON
  const data = JSON.parse(body);

  // Filter completed tasks
  const completedTasks = data.filter(task => task.completed);

  // Compute the number of completed tasks by user ID
  const completedTasksByUser = completedTasks.reduce((acc, task) => {
    acc[task.userId] = (acc[task.userId] || 0) + 1;
    return acc;
  }, {});

  console.log(completedTasksByUser);
});
