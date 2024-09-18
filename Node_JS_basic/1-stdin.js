#!/usr/bin/env node

console.log("Welcome to Holberton School, what is your name?");

// Active stdin
process.stdin.resume();
process.stdin.setEncoding('utf-8');

// Écoute de l'entrée
process.stdin.on('data', function(data) {
  const name = data.trim();
  console.log(`Your name is: ${name}`);
});

// Écoute la fin de l'entrée
process.stdin.on('end', function() {
  console.log('This important software is now closing');
});
