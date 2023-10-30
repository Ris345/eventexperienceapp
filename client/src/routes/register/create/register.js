import { goto } from '$app/navigation';

export const createAndSubmit = async (form) => {
  console.log('submitting registration information');
  // logic to send to backend running on port 8000 to route '/users'
  fetch('http://127.0.0.1:8000/users', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      username: form.userName,
      first_name: form.firstName,
      last_name: form.lastName,
      email: form.email,
      profile_photo: form.profile_photo,
      about: form.about,
      password: form.password
    }).toString()
    })
    .then(async (response) => {
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(`${errorData.detail}`);
      }
      return response.json();
    })
    .then((user) => {
      console.log(user);
    })
    .then(async () => {
      await fetch('http://127.0.0.1:8000/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
          },
        body: new URLSearchParams({
        username: form.userName,
        password: form.password
        }).toString()
      })
      .then(async (response) => {
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(`${errorData.detail}`);
        }
        return response.json();
      })
      .then((result) => {
        console.log(result);
        localStorage.setItem('eea-user-access-token',result.access_token);
        goto('/');
      })
      .catch((error) => {
        console.log(`Error: ${error}`);
      })
    })
    .catch((error) => {
      console.log(`Error with the fetch operation: ${error}`);
    })
};
