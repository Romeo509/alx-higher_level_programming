#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  const uniqueNumbers = [...new Set(numbers)]; // Remove duplicates
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a); // Sort in descending order
  console.log(sortedNumbers[1]);
}
