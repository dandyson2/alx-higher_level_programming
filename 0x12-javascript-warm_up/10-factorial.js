#!/usr/bin/node

function factorial(n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const inputNumber = Number(process.argv[2]);

if (!isNaN(inputNumber)) {
  console.log(factorial(inputNumber));
} else {
  console.error("Invalid input. Please provide a valid number.");
}
