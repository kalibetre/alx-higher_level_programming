#!/usr/bin/node
exports.esrever = function (list) {
  return list.map(list.pop, [...list]);
};
