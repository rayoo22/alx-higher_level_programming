#!/usr/bin/node

const ag = parseInt(process.argv[2]);

if (isNaN(ag))
{
	console.log('Not a number');
}
else
{
	console.log('My number:', ag);
}
