#!/usr/bin/node
const axios = require('axios');

async function fetchFilmCharacters(filmId) {
  try {
    const response = await axios.get(`https://swapi-api.hbtn.io/api/films/${filmId}`);
    const characters = response.data.characters;
    await printCharacters(characters, 0);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  try {
    const response = await axios.get(characters[index]);
    console.log(response.data.name);
    await printCharacters(characters, index + 1);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

const filmId = process.argv[2];
if (filmId) {
  fetchFilmCharacters(filmId);
} else {
  console.error('Please provide a valid film ID as a command-line argument.');
}
