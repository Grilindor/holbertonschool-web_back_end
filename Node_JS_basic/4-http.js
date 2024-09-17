const http = require('http');

const app = http.createServer((req, res) =>{

  res.writeHead(200, { 'content-Type': 'text/plain' });

  res.end('Hello Holberton School!');

});

app.listen(1245);

module.exports = app;
