#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(x => parseInt(x)).sort((a, b) => b - a);
  console.log(numbers[1] || 0);
}
