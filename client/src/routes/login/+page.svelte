<script>
	import Button, { Label } from '@smui/button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	let username = '',
		password = '';
	$: console.log(username);
	$: console.log(password);

	const handleOnSubmit = (e) => {
		e.preventDefault()
		console.log('submitting login information');
	};
</script>

<main>
	<h2>Login</h2>
	<form on:submit={handleOnSubmit}>
		<Textfield bind:value={username} label="Username" />

		<Textfield bind:value={password} type="password" label="Password" />

		<Button variant="raised" type="submit"><Label>Login</Label></Button>
	</form>
</main>

<style>
	form {
		display: grid;
		grid-template-columns: 1fr 1fr;
		width: max-content;
		gap: 1em;
		background: #000000bb;
		padding: 1em;
		box-shadow: 0px 0px 20px 20px #000000bb;
	}
	h2 {
		color: white;
		margin: 0.25em 0;
	}
</style>
