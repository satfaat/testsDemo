alert("Привет, NodeJS");
const testLib = require('./test-lib.js');
const http = require('http'); 
console.log(http.METHODS); // обратились к METHODS в модуле http