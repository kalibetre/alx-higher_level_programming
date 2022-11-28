#!/usr/bin/node
module.exports.callMeMoby = function (x, theFunction) {
  while (x-- > 0) theFunction();
};
