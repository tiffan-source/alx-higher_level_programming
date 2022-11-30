#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i;
    if (c === undefined) { c = 'X'; }
    const toPrint = c.repeat(this.width);
    for (i = 0; i < this.width; i++) {
      console.log(toPrint);
    }
  }
};
