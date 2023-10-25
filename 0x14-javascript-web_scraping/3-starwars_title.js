#!/usr/bin/node

const request = require('request');

const baseUrl = 'http://swapi.co/api/films/';
const filmId = process.argv[2];
const url = `${baseUrl}${filmId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
