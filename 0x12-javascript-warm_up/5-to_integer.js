#!/usr/bin/node
const arg = process.argv[2];
const argAsInt = parseInt(arg);
if (Number.isNaN(argAsInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argAsInt);
}
