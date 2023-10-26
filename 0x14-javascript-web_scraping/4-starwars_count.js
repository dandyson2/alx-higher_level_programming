#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    const count = movies.reduce((total, movie) => {
      const hasCharacterEndingWith18 = movie.characters.some((character) => character.endsWith('/18/'));
      return hasCharacterEndingWith18 ? total + 1 : total;
    }, 0);

    console.log(count);
  }
});
