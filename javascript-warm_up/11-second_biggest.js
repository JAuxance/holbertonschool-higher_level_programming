#!/usr/bin/node
const numbers = process.argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  let biggest = -Infinity;
  let secondBiggest = -Infinity;

  for (const num of numbers) {
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num !== biggest) {
      secondBiggest = num;
    }
  }

  console.log(secondBiggest);
}
