#!/usr/bin/node
if (process.argv[2] && process.argv[3] !== null) {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
} else if (process.argv[2] === null) {
  console.log('undefined is' + process.argv[3]);
} else if (process.argv[3] === null) {
  console.log(process.argv[2] + ' ' + 'is undefined');
} else {
  console.log('undefined is undefined');
}
