#!/usr/bin/node

const request = require('request');

const statusCode = (url) => {
  request.get(url, (error, response) => {
    if (error) {
      console.error('code:', error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
};

const url = process.argv[2];
statusCode(url);
