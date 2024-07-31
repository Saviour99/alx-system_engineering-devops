#!/usr/bin/node

const fs = require('fs');

const readFile = (filePath) => {
  try {
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    console.log(fileContent);
  } catch (err) {
    console.error(err);
  }
};

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readFile(filePath);
