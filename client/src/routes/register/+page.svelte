<script>
	import Button, { Label } from '@smui/button';
	import SegmentedButton, { Segment } from '@smui/segmented-button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	import axios from 'axios';
	import { createEventDispatcher } from 'svelte';

	let invalid = false,
		firstName = '',
		lastName = '',
		email = '',
		password = '',
		selectedRole;
	const choices = ['Admin', 'Organizer', 'Volunteer'];
	const dispatch = createEventDispatcher();
	// handleSubmit
	const handleOnSubmit = async (e) => {
		e.preventDefault();
		console.log('submitting  the data to the back end ');
		// make a post request
		try {
			const response = await axios.post('/api/backend', { firstName, lastName, password, email });
			dispatch('formSubmitted', response.data);
		} catch (error) {
			console.error(error);
		}
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
		<Textfield bind:value={firstName} label="First Name" required />

		<Textfield bind:value={lastName} label="Last Name" required />

		<Textfield bind:value={email} type="email" bind:invalid updateInvalid label="Email" required>
			<HelperText validationMsg slot="helper">Please enter a valid email address.</HelperText>
		</Textfield>
		<Textfield bind:value={password} label="Password" type="password">
			<HelperText slot="helper">Your password must be stronger.</HelperText>
		</Textfield>
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
		color: white;
		margin: 0.25em 0;
	}
	form {
		display: grid;
		grid-template-columns: auto auto;
		justify-items: baseline;
		width: max-content;
		gap: 1em;
		background: #000000bb;
		padding: 1em;
		box-shadow: 0px 0px 20px 20px #000000bb;
	}
</style>
