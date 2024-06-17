#!/usr/bin/node
const ls = process.argv;

if (ls.length === 2) {
  console.log(0);
} else if (ls[2] == 1) {
  console.log(0);
} else {
  ls.sort();
  console.log(ls[ls.length - 2]);
}
