#!/usr/bin/node

const request = require('request');
const apiUrl = 'http://swapi.co/api/films/';
const filmId = process.argv[2];
const url = `${apiUrl}${filmId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  }
});
