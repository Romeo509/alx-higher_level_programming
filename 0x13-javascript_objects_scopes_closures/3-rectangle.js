#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If width or height is 0 or not a positive integer, create an empty object
      const emptyObject = {};
      Object.assign(this, emptyObject);
    } else {
      // Initialize instance attributes with the provided values
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      // If width and height are valid, print the rectangle using the character X
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
