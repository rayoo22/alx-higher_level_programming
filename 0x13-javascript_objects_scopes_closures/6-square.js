#!/usr/bin/node

//importing file 5-square.js
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
	constructor(size){
		//calling cinstructor of parent class
		super(size, size);
	}
	//instance method to print the squareusing character C
	charPrint(c){
		if (typeof c === 'undefined'){
			c = 'X';
		}
		
		for (let i = 0; i < this.height; i++){
			let row = '';
			for (let j = 0; j < this.width; j++){
				row += c;
			}
			console.log(row);
		}
	}
};
