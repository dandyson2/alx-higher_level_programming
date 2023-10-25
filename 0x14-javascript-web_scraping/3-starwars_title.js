#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = `http://swapi.co/api/films/${filmId}`;

const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
};

fetchData(url)
  .then((body) => {
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  })
  .catch((error) => {
    console.error(error);
  });
