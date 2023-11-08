<script>
	import Button, { Label } from '@smui/button';
	import SegmentedButton, { Segment } from '@smui/segmented-button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	import { createAndSubmit } from './create/register.js';

	let invalid = false;
	let userName = '';
	let firstName = '';
	let lastName = '';
	let email = '';
	let profile_photo = '';
	let about = '';
	let password = '';
	let selectedRole;

	const choices = ['Admin', 'Organizer', 'Volunteer'];

	// handleSubmit; logic to send to backend
	async function handleOnSubmit(event) {
		event.preventDefault();
		const form = {
			userName,
			firstName,
			lastName,
			email,
			profile_photo,
			about,
			password,
			selectedRole
		};
		await createAndSubmit(form);
	}

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
