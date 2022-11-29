#!/usr/bin/node
function logger () {
  let logCount = 0;
  return (item) => {
    console.log('%i: %s', logCount++, item);
  };
}

exports.logMe = logger();
