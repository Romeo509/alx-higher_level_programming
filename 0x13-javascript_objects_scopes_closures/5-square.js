#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the parent class (Rectangle) using super()
    super(size, size);
  }
}

module.exports = Square;
