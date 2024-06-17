#!/usr/bin/node

let args = process.argv;

if (args[1] == null) {
	console.log("No argument");
}
else {
	console.log(args[1]);
}
