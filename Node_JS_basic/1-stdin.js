console.log("Welcome to Holberton School, what is your name?");

// Active stdin
process.stdin.resume();
process.stdin.setEncoding('utf-8');

// Variable pour stocker l'entrée de l'utilisateur
let inputData = '';

// Écouter les données de l'utilisateur
process.stdin.on('data', function(data) {
  inputData += data;
});

// Écouter la fin de l'entrée (utile pour le pipe avec echo)
process.stdin.on('end', function() {
  const name = inputData.trim();
  console.log(`Your name is: ${name}`);
  console.log('This important software is now closing');
  process.exit();
});
