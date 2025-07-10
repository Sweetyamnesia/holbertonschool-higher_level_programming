#!/usr/bin/node
const messages = [
  "C is fun",
  "Python is cool",
  "JavaScript is amazing"
];

let sentences = "";
for (let i = 0; i < messages.length; i++) {
  sentences += messages[i] + "\n";
}

console.log(sentences);
