#!/usr/bin/node

const request = require('request');

const getMoviesWithCharacter = (apiUrl, characterId) => {
  const url = `${apiUrl}`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movies = JSON.parse(body).results;
      const moviesWithCharacter = movies.filter(movie => {
        const characterUrls = movie.characters;
        const characterUrl = `${apiUrl}people/${characterId}/`;
        return characterUrls.includes(characterUrl);
      });
      console.log(moviesWithCharacter.length);
    }
  });
};

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;
getMoviesWithCharacter(apiUrl, characterId);
