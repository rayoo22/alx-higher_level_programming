#!/usr/bin/node
// prints the addition of 2 integers
// using 2 command line arguments
const argument = process.argv;
const firstArg = parseInt(argument[2]);
const secondArg = parseInt(argument[3]);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

if ((isNaN(firstArg) && isNaN(secondArg)) || argument.length === 2) {
  console.log('NaN');
} else {
  add(firstArg, secondArg);
}
