#!/usr/bin/node

const request = require('request');

function checkStatusCode(url) {
  request.get(url).on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
}

const url = process.argv[2];
checkStatusCode(url);
