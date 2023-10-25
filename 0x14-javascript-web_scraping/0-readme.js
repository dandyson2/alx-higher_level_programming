#!/usr/bin/node

const fs = require('fs');

function readFileContent(filePath) {
  fs.readFile(filePath, 'utf8', (error, content) => {
    console.log(error || content);
  });
}

const filePath = process.argv[2];
readFileContent(filePath);
