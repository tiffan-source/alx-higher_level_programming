#!/usr/bin/node
let list = require('./100-data').list;

console.log(list);

list = list.map((data, index) => {
  return data * index;
});

console.log(list);
