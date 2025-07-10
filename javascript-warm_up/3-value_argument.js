#!/usr/bin/env node
const args = require('node:process');

if (args === 0) {
  console.log("No argument");
} else {
  console.log(args);
}
