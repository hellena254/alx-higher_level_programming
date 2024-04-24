#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
