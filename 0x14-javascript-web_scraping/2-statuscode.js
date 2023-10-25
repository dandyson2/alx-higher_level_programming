#!/usr/bin/node
const axios = require('axios');

async function getRequest() {
  try {
    const response = await axios.get(process.argv[2]);
    console.log(`code: ${response.status}`);
  } catch (error) {
    console.error(error.message);
  }
}

getRequest();
