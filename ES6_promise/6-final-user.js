import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  // create a const with the function 4 and 5 (whit await) who wait the result of these promises
  const result = await Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]);
  // map the results in a array with = statut, value, error message
  return result.map((result) => ({
    status: result.status,
    value: result.status === 'fulfilled' ? result.value : `Error: ${result.reason.message}`,
  }));
}
