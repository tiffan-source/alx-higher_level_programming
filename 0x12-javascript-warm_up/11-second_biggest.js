#!/usr/bin/node

let array = process.argv.slice(2);

array = array.map(x => Number.parseInt(x));

array.sort((a, b) => (b - a));

if (array.length === 0 || array.length === 1) {
  console.log(0);
} else {
  console.log(array[1]);
}
