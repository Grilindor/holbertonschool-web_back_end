const http = require('http');
const countStudents = require('./3-read_file_async');  // Importation de la fonction

const app = http.createServer(async (req, res) => {
  const url = req.url;

  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    const database = process.argv[2];  // Le fichier CSV est passé en argument
    if (!database) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Database not provided');
      return;
    }

    try {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.write('This is the list of our students\n');

      // Appel de la fonction countStudents
      await countStudents(database);
      res.end();
    } catch (error) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end(error.message);
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
