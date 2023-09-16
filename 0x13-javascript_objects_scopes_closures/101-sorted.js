#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};

Object.entries(dict).forEach(([key, value]) => {
  newDict[value] = newDict[value] || [];
  newDict[value].push(key);
});

console.log(newDict);
