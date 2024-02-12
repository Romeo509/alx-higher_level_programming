#!/usr/bin/node

const numOccurrences = parseInt(process.argv[2]);

if (isNaN(numOccurrences) || numOccurrences < 1) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
