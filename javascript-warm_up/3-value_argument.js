#!/usr/bin/node
const { args } = require('node:process');

if (process.args < 3) {
  console.log("No argument");
} else {
  console.log(process.argv);
}