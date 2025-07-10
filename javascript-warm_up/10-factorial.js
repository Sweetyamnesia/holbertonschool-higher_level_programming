#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2]);

const factorial = n => (isNaN(n) || n <= 1) ? 1 : n * factorial(n - 1);

console.log(factorial(num));
