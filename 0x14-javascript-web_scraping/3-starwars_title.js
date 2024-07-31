#!/usr/bin/node

const requests = require('request');

const movieTitle = (episodeId) => {
  const baseUrl = 'https://swapi-api.alx-tools.com/api/films';
  const url = `${baseUrl}/${episodeId}`;
  requests.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  });
};
const episodeId = process.argv[2];
movieTitle(episodeId);
