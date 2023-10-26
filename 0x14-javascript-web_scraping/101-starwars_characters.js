#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.error('Error:', error);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return; // Base case: all characters have been printed
  }

  request(characters[index], function (error, response, body) {
    if (!error) {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      printCharacters(characters, index + 1); // Recursively print the next character
    } else {
      console.error('Error:', error);
    }
  });
}
