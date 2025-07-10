#!/usr/bin/node
const args = process.argv;
function add(a, b){
	return a + b;
}

const num1 = parseInt(args[2], [10]);
const num2 = parseInt(args[3], [10]);

console.log(num1 + num2);
