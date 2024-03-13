#!/usr/bin/node
// searches for the second biggest integer in a list of arguments
const args = process.argv.slice(2).map(Number);

if (args.length === 0) {
  // if no arguments were passed
  console.log(0);
} else if (args.length <= 1) {
  // if 1 argument was passed
  console.log(0);
} else {
  args.sort((a, b) => b - a); // sorts in ascending order
  console.log(args[1]);
}
