const http = require('http');
const fs = require('fs');
const path = require('path');

function countStudents(database) {
  return new Promise((resolve, reject) => {
    fs.readFile(database, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const fields = {};
      let totalStudents = 0;

      for (const line of lines.slice(1)) {
        const [firstName, lastName, age, field] = line.split(',');

        if (!firstName || !lastName || !age || !field) {
          continue;
        }

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
        totalStudents += 1;
      }

      resolve({ totalStudents, fields });
    });
  });
}

const app = http.createServer((req, res) => {
  const url = req.url;

  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    const database = process.argv[2];
    if (!database) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Database not provided');
      return;
    }

    countStudents(database)
      .then((result) => {
        const { totalStudents, fields } = result;
        let responseText = 'This is the list of our students\n';
        responseText += `Number of students: ${totalStudents}\n`;

        for (const [field, students] of Object.entries(fields)) {
          responseText += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
        }

        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(responseText);
      })
      .catch((error) => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(error.message);
      });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
