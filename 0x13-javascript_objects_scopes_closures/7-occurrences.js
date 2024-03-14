#!/usr/bin/node
// returns the number of occurrences a value appears in a list
exports.nbOccurrences = function (list, searchElement) {
  let num = 0;

  for (let i = 1; i <= list.length; i++) {
    if (list[i] === searchElement) {
      num += 1;
    }
  }
  return (num);
};
