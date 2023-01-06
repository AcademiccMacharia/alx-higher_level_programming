#!/usr/bin/node
const arg = process.argv[2];
let argAsInt = parseInt(arg);
if (Number.isNaN(argAsInt)) {
  console.log('Missing number of occurences');
} else {
  while (argAsInt > 0) {
    console.log('C is fun');
    argAsInt--;
  }
}
