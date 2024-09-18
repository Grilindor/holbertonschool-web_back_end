const express = require('express');
const fs = require('fs');
const path = require('path');

// Créer l'application Express
const app = express();

// Fonction pour lire et compter les étudiants
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
          continue; // Ignorer les lignes vides ou incorrectes
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

// Route pour l'URL racine '/'
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route pour '/students'
app.get('/students', (req, res) => {
  const database = process.argv[2];
  if (!database) {
    res.status(500).send('Database not provided');
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

      res.send(responseText);
    })
    .catch((error) => {
      res.status(500).send(error.message);
    });
});

// Le serveur écoute sur le port 1245
app.listen(1245, () => {
  console.log('Serveur en écoute sur le port 1245');
});

// Exporter l'application Express
module.exports = app;
