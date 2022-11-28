#!/usr/bin/node

function findSecondBiggest (values) {
  if (values.length <= 1) return 0;
  return values.sort((a, b) => a - b).reverse()[1];
}

const nums = process.argv.slice(2).map((x) => parseInt(x, 10));
console.log(findSecondBiggest(nums));
