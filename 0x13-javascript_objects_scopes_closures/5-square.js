#!/usr/bin/node
// importing 4-rectangle.js
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    // size property will replace width and height
    super(size, size);
  }
};
