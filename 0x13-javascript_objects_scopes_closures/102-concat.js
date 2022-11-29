#!/usr/bin/node
const fs = require('fs');

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const targetFile = process.argv[4];

if (fs.existsSync(firstFile) && fs.existsSync(secondFile)) {
  fs.writeFileSync(targetFile, fs.readFileSync(firstFile));
  fs.appendFileSync(targetFile, fs.readFileSync(secondFile));
}
