#!/usr/bin/node
const arg = process.argv[2];
const argAsInt = parseInt(arg);
let i, j, s;
if (Number.isNaN(argAsInt)) {
  console.log('Missing size');
} else {
  for (i = 0; i < argAsInt; i++) {
    s = ' ';
    for (j = 0; j < argAsInt; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
