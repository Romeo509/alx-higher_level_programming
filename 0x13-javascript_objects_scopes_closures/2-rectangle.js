#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If width or height is 0 or not a positive integer, create an empty object
      return {};
    }

    // Initialize instance attributes with the provided values
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
