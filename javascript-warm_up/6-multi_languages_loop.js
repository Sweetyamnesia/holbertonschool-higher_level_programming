#!/usr/bin/node
const messages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

const result = [];

for (let i = 0; i < messages.length; i++) {
  result.push(messages[i]);
}

console.log(result.join('\n'));
