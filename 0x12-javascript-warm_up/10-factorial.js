#!/usr/bin/node

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  }
  if (number <= 1) {
    return 1;
  }
  return number * factorial(number - 1);
}

const arg = parseInt(process.argv[2]);

console.log(factorial(arg));
