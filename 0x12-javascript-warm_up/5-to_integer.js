#!/usr/bin/node
const args = process.argv;

if (!parseInt(args[2])) {
  console.log('Not a number');
} else {
  const res = parseInt(args[2]);
  console.log('My number: ' + res);
}
