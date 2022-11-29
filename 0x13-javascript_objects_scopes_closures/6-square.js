#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    const ch = typeof c === 'undefined' ? 'X' : c;
    console.log(this.toString(ch));
  }
}

module.exports = Square;
