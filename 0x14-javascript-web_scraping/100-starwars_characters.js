#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request.get(characterUrl, function (error, response, characterBody) {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
