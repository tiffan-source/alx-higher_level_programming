#!/usr/bin/node

const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c) {
    let i;
    if (c === undefined) { c = 'X'; }
    const toPrint = c.repeat(this.width);
    for (i = 0; i < this.width; i++) {
      console.log(toPrint);
    }
  }
};
