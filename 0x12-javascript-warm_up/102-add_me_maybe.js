#!/usr/bin/node

const addMeMaybe = (number, theFunction) => {
  theFunction(++number);
};

module.exports = { addMeMaybe };
