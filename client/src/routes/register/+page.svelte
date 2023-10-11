<script>
	import Button, { Label } from '@smui/button';
	import SegmentedButton, { Segment } from '@smui/segmented-button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	import { redirect } from '@sveltejs/kit'
	import { goto } from '$app/navigation';

	let invalid = false,
		userName = '',
		firstName = '',
		lastName = '',
		email = '',
		profile_photo = '',
		about = '',
		password = '',
		selectedRole;
	const choices = ['Admin', 'Organizer', 'Volunteer'];
	// handleSubmit
	const handleOnSubmit = async (event) => {
		event.preventDefault();
		console.log('submitting registration information');
		// logic to send to backend running on port 8000 to route '/users'
		fetch('http://127.0.0.1:8000/users', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			body: new URLSearchParams({
				username: userName,
				first_name: firstName,
				last_name: lastName,
				email: email,
				profile_photo: profile_photo,
				about: about,
				password: password
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
					username: userName,
					password: password
					}).toString()
				})
				.then(async (response) => {
					if (!response.ok) {
						const errorData = await response.json();
						throw new Error(`${errorData.detail}`);
					}
					return response.json();
				})
				.then((token) => {
					console.log(token);
					//trying to get this to work
					// event.cookies.set(token, {
					// 	httpOnly: true,
					// 	path: '/',
					// 	secure: true,
					// 	sameSite: 'strict',
					// 	maxAge: 60 * 60 * 24
					// })
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








	//change client view to dashboard/home page
	
	
	$: console.log('First_name', firstName);

	$: console.log('Last_name', lastName);

	$: console.log('E_mail', email);
	$: console.log('Pass_word', password);
	$: console.log('selected_role', selectedRole);
</script>

<main>
	<h2>Register</h2>
	<form on:submit={handleOnSubmit}>
		<Textfield bind:value={userName} label="Username" required />
		<Textfield bind:value={firstName} label="First Name" required />

		<Textfield bind:value={lastName} label="Last Name" required />

		<Textfield bind:value={email} type="email" bind:invalid updateInvalid label="Email" required>
			<HelperText validationMsg slot="helper">Please enter a valid email address.</HelperText>
		</Textfield>
		<Textfield bind:value={profile_photo} label="Profile Photo" />
		<Textfield bind:value={password} label="Password" type="password" required>
			<HelperText slot="helper">Your password must be stronger.</HelperText>
		</Textfield>
		<Textfield bind:value={about} label="About" />
		<SegmentedButton
			style="grid-column: span 2;"
			segments={choices}
			let:segment
			singleSelect
			bind:selected={selectedRole}
		>
			<Segment type="button" {segment}>
				<Label>{segment}</Label>
			</Segment>
		</SegmentedButton>
		<Button variant="raised" type="submit">
			<Label>Register</Label>
		</Button>
	</form>
</main>

<style>
	h2 {
		color: rgb(0, 0, 0);
		margin: 0.25em 0;
	}
	form {
		display: grid;
		grid-template-columns: auto auto;
		justify-items: baseline;
		width: max-content;
		gap: 1em;
		background: #ffffffbb;
		padding: 1em;
		box-shadow: 0px 0px 20px 20px #000000bb;
	}
</style>
