#!/usr/bin/node

const request = require('request');
const charId = '18';
const apiUrl = process.argv[2];
let count = 0;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}`)) {
        count++;
      }
    });
    console.log(count);
  }
});
