export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => (
      // Handler for resolve of promise
      {
        status: 200,
        body: 'success',
      }))
    .catch(() => Error())
    // Handler for the reject of the promise

    .finally(() => {
      // Handler who run in any case
      console.log('Got a response from the API');
    });
}
