<script>
	import Button, { Label } from '@smui/button';
	import SegmentedButton, { Segment } from '@smui/segmented-button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	let invalid = false,
		firstName = '',
		lastName = '',
		email = '',
		password = '',
		selectedRole;
	const choices = ['Admin', 'Organizer', 'Volunteer'];
</script>

<main>
	<h2>Register</h2>
	<form method="POST">
		<Textfield bind:value={firstName} label="First Name" />

		<Textfield bind:value={lastName} label="Last Name" />

		<Textfield bind:value={email} type="email" bind:invalid updateInvalid label="Email">
			<HelperText validationMsg slot="helper">Please enter a valid email address.</HelperText>
		</Textfield>
		<Textfield bind:value={password} label="Password">
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
