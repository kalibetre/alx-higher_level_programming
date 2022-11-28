#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 0) return 1;
  else if (num < 0) return NaN;

  let fact = 1;
  if (!isNaN(num)) {
    while (num > 1) fact *= num--;
  }
  return fact;
}

console.log(factorial(parseInt(process.argv[2], 10)));
