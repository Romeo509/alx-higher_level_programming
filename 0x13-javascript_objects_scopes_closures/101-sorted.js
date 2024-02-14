#!/usr/bin/node
const { dict } = require('./101-data');

const occurrencesByUser = {};

// Loop through the original dictionary to compute the new dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  if (!occurrencesByUser[occurrences]) {
    occurrencesByUser[occurrences] = [];
  }

  occurrencesByUser[occurrences].push(userId.toString());
}

// Print the new dictionary
console.log(occurrencesByUser);
