#!/usr/bin/node

const nbOccurences = function countOccurrences(list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};

exports.nbOccurences = nbOccurences;
