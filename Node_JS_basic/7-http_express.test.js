const request = require('supertest');
const app = require('./7-http_express'); // Importer l'app Express

describe('Test the root path', () => {
  test('It should respond with "Hello Holberton School!"', async () => {
    const response = await request(app).get('/');
    expect(response.text).toBe('Hello Holberton School!');
    expect(response.statusCode).toBe(200);
  });
});

describe('Test the /students path', () => {
  test('It should respond with "This is the list of our students"', async () => {
    const response = await request(app).get('/students');
    expect(response.text).toContain('This is the list of our students');
    expect(response.statusCode).toBe(200);
  });
});
