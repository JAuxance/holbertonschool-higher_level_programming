#!/usr/bin/node
const xLog = parseInt(process.argv[2]);
let a = 0;
if (isNaN(xLog)) {
  console.log('Missing number of occurrences');
} else {
  while (a < xLog) {
    console.log('C is fun');
    a = a + 1;
  }
}
