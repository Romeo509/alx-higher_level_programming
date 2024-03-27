#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error(new Error('Usage: ./3-starwars_title.js <movie_id>'));
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API to fetch movie details
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Parse the response body to JSON
  const movie = JSON.parse(body);

  // Print the title of the movie
  console.log(movie.title);
});
