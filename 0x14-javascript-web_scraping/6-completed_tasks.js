#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Unexpected status code ${response.statusCode}`);
  } else {
    try {
      const todos = JSON.parse(body);
      const completedCounts = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          completedCounts[todo.userId] = (completedCounts[todo.userId] || 0) + 1;
        }
      });

      console.log(completedCounts);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});
