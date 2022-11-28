#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const numOne = Number.parseInt(process.argv[2]);
const numTwo = Number.parseInt(process.argv[3]);
add(numOne, numTwo);
