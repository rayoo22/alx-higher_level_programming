#!/usr/bin/node
// creates rectangle clas, with instance attributes
// If w or h is equal to 0 or not a positive integer, create an empty object
module.exports = class Rectangle {
	constructor(w, h){
		if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h))
			//if h or w are not positive integers
		{
			return {};
		}

		this.width = w;
		this.height = h;
	}
};
