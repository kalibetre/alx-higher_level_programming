#!/usr/bin/node
function factorial (num) {
  let fact = 1;
  if (!Number.isNaN(num)) {
    while (num > 1) fact *= num--;
  }
  console.log(fact);
}
const num = Number.parseInt(process.argv[2]);
factorial(num);
