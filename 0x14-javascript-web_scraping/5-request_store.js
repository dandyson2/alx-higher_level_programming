#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const fetchAndSaveWebpage = (url, filePath) => {
    request(url, (error, response, body) => {
        if (error) {
            console.error(`Error: ${error}`);
        } else {
            fs.writeFile(filePath, body, 'utf-8', (err) => {
                if (err) {
                    console.error(`Error writing to file: ${err}`);
                } else {
                    console.log(`Webpage content successfully saved to: ${filePath}`);
                }
            });
        }
    });
};

const [, , url, filePath] = process.argv;

if (url && filePath) {
    fetchAndSaveWebpage(url, filePath);
} else {
    console.error('Usage: node script.js <URL> <FilePath>');
}
