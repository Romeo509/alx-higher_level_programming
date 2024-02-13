#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If width or height is 0 or not positive, create an empty object
      return {};
    }

    // Initialize instance attributes with the provided values
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
