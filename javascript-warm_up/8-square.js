#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
let i = 0;

if (isNaN(size)) {
  console.log("Missing size");
} else {
  while (i < size) {
	let line = "";
	let j = 0;
    while (j < size) {
		line += "X";
		j++;
	}
	console.log(line)
	i++;
  }
}
