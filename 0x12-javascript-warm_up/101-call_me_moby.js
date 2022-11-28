#!/usr/bin/node
module.exports.callMeMoby = function (x, theFunction) {
  while (x--) theFunction();
};
