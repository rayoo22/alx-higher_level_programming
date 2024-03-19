#!/usr/bin/node
// computes recursion
const argument = process.argv;
const number = argument[2];

function factorial (number) {
  if (number <= 1 || isNaN(number)) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
console.log(factorial(number));
