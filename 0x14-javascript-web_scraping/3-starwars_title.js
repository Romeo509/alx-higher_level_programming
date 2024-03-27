#!/usr/bin/node

const url = 'http://swapi.co/api/films/';
const argv = process.argv;
const request = require('request');

request(url + argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
