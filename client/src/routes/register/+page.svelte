<script>
	import Button, { Label } from '@smui/button';
	import SegmentedButton, { Segment } from '@smui/segmented-button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	import axios from 'axios';
	import { createEventDispatcher } from 'svelte';

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
	const dispatch = createEventDispatcher();
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
			body: new URLSearchParams({ username: userName, 
					first_name: firstName,
					last_name: lastName, 
					email: email, 
					profile_photo: profile_photo,
					about: about, 
					password: password }).toString()
		})
		.then(response => {
			if (!response.ok) {
				console.error(response.json)
				throw new Error('Network response was not ok');
			}
			return response.json();
		})
		.then(result => {
			console.log(result);
		})
		.catch(error => {
			console.log(`Error with the fetch operation: ${error}`)
		})
	};

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
