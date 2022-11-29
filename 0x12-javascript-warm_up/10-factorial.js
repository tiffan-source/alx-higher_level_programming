#!/usr/bin/node

function factorial (number) {
  if (Number.isNaN(number) || number <= 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

const number = Number.parseInt(process.argv[2]);

console.log(factorial(number));
