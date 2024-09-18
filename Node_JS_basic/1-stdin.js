console.log("Welcome to Holberton School, what is your name?");

// Active stdin
process.stdin.resume();
process.stdin.setEncoding('utf-8');

// Fonction principale
function askName() {
  // Écoute l'entrée de l'utilisateur
  process.stdin.on('data', function(data) {
    const name = data.trim();
    console.log(`Your name is: ${name}`);

    console.log('This important software is now closing');
    process.exit();
  });
}

// Exporte la fonction
module.exports = askName;
