#!/usr/bin/node
module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
