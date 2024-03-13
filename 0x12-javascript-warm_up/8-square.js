#!/usr/bin/node
// converts argument to an integer
const argument = parseInt(process.argv[2]);
// to check if the argument can't be converted to an integer
if (isNaN(argument)) {
  console.log('Missing Size');
} else {
  for (let i = 0; i < argument; i++) {
    let line = '';
    for (let j = 0; j < argument; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
