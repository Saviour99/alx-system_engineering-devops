#!/usr/bin/node

const requests = require('request');
const fs = require('fs');

const getTheContent = (url, filePath) => {
  requests.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFileSync(filePath, body, 'utf-8');
    }
  });
};

const url = process.argv[2];
const filePath = process.argv[3];

getTheContent(url, filePath);
