#!/usr/bin/node

let occur = Number.parseInt(process.argv[2]);
const i = occur;

if (Number.isInteger(occur)) {
  while (occur > 0) {
    console.log('X'.repeat(i));
    occur--;
  }
} else {
  console.log('Missing size');
}
