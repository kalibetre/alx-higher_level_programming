#!/usr/bin/node
function factorial (num) {
  let fact = 1;
  if (!isNaN(num)) {
    while (num > 1) fact *= num--;
  }
  return fact;
}

console.log(factorial(parseInt(process.argv[2], 10)));
