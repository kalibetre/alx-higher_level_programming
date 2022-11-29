#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const ch = typeof c === 'undefined' ? 'X' : c;
    console.log(this.toString(ch));
  }
}

module.exports = Square;
