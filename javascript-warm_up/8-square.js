#!/usr/bin/node
const size = parseInt(process.argv[2]);
let a = 0;
let b = 0;
let xCreator = [];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (a < size) {
    xCreator = xCreator + ['X'];
    a = a + 1;
  }
  while (b < size) {
    console.log(xCreator);
    b = b + 1;
  }
}
