#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log("Please provide two arguments");
} else {
  console.log(`${args[0]} is ${args[1]}`);
}