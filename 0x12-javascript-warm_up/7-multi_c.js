#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv === undefined) {
  console.log('Missing number of occurences');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
