#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2]);
let i = 0;
let j = 0;
let line = "";

if (isNaN(size)) {
  console.log("Missing size");
} else {
  while (i < size) {
    while (j < size) {
		line += "X";
		j++;
	}
	console.log(line)
	i++;
  }
}
