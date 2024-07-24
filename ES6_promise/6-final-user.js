import signUpUser from './4-user-promise'
import uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  const result = await Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]);
  return result.map((result) => ({
    status: result.status,
    value: result.status === 'rejected' ? result.value : `Error: ${result.reason.message}`,
  }));
}
