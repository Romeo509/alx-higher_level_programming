#!/usr/bin/node

const url = 'http://swapi.co/api/films/';
const argv = process.argv;
const request = require('request');

try {
    request(url + argv[2], function (err, res, body) {
        if (err) {
            console.error('Error occurred:', err);
            process.exit(1);
        }
        try {
            const json = JSON.parse(body);
            console.log(json.title);
        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
            process.exit(1);
        }
    });
} catch (requestError) {
    console.error('Error making request:', requestError);
    process.exit(1);
}
