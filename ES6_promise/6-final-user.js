import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const data = await Promise.allSettled([uploadPhoto(filename), signUpUser(firstName, lastName)]);
  return data
    .map((item) => ({
      status: item.status,
      value: item.reason ? item.reason.message : item.value,
    }));
}
