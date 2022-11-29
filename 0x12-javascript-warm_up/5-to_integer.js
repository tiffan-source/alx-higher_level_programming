#!/usr/bin/node

const arg = Number.parseInt(process.argv[2]);

if (!Number.isInteger(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
