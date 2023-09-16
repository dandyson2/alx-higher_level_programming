#!/usr/bin/node

const fs = require('fs');

// Read the contents of the first file specified in the command line arguments
const file1Contents = fs.readFileSync(process.argv[2], 'utf8');

// Read the contents of the second file specified in the command line arguments
const file2Contents = fs.readFileSync(process.argv[3], 'utf8');

// Combine the contents of both files and write them to a new file specified in the command line arguments
fs.writeFileSync(process.argv[4], file1Contents + file2Contents);
