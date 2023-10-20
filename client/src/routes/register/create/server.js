export async function createAndSubmit(form) {
    console.log('submitting registration information');
    try {
        const formData = new URLSearchParams({
            username: form.userName,
            first_name: form.firstName,
            last_name: form.astName,
            email: form.email,
            profile_photo: form.profile_photo,
            about: form.about,
            password: form.password
        }).toString()
    
      const user = await fetch('http://127.0.0.1:8000/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData,
      })
        .then(async (response) => {
          if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`${errorData.detail}`);
          }
          return response.json();
        });
  
      const token = await fetch('http://127.0.0.1:8000/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          username: user.username,
          password: user.password,
        }).toString(),
      })
        .then(async (response) => {
          if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`${errorData.detail}`);
          }
          return response.json();
        });
  
      console.log(token);
      goto('/');
    } catch (error) {
      console.log(`Error: ${error}`);
      console.log(`Error with the fetch operation: ${error}`);
    }
  }
  