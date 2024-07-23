export default function getResponseFromAPI() {
  // return a new obj promise
  return new Promise((response) => {
    // call response function, solving the promise
    response();
  });
}
