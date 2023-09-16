#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let y = 0;
  while (y < size) {
    let row = '';
    let z = 0;
    while (z < size) {
      row += 'X';
      z++;
    }
    console.log(row);
    y++;
  }
}
