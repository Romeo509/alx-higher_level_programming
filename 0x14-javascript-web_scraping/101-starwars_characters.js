#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error(new Error('Usage: ./101-starwars_characters.js <movie_id>'));
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a GET request to the Star Wars API to fetch movie details
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Parse the response body to JSON
  const film = JSON.parse(body);

  // Fetch characters associated with the movie
  const charactersUrls = film.characters;

  // Function to fetch and print character names
  const printCharacters = (index) => {
    if (index === charactersUrls.length) {
      return;
    }
    request.get(charactersUrls[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(index + 1);
    });
  };

  // Start printing character names
  printCharacters(0);
});
