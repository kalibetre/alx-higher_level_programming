#!/usr/bin/node
let count = Number.parseInt(process.argv[2]);
if (Number.isNaN(count)) console.log('Missing number of occurrences');
else {
  while (count--) console.log('C is fun');
}
