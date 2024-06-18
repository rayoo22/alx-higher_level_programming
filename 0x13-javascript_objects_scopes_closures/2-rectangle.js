#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
	  if (w <= 0 || h <= 0) {
		  //if arguments are less than 0, it returns nothing
		  return;
	  }
	  this.width = w;
	  this.height = h;
  }
};
