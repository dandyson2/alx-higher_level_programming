#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
        const movieData = JSON.parse(body);
        console.log(`Title of Star Wars Episode ${movieID}: ${movieData.title}`);
    } else {
        console.log('Error fetching data from the API.');
    }
});
