<script>
	import Button, { Label } from '@smui/button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	import { createEventDispatcher } from 'svelte';
	import axios from 'axios';
	import placeholder from "./assets/placeholder-login.jpeg"
	// import FacebookIcon from '@mui/icons-material/Facebook';

	let username = '',
		password = '';
	$: console.log(username);
	$: console.log(password);
	const dispatch = createEventDispatcher();

	// final commit before moving on 

	const handleOnSubmit = async  (e) => {
		e.preventDefault()
		console.log('submitting login information');
		// submit post request 
		try {
			const response = await axios.post('/api/backend', { username, password });
			dispatch('formSubmitted', response.data);
		} catch (error) {
			console.error(error);
		}
	};
</script>

<main>
	<h2>Login</h2>
	<div class="container">
		<img src={placeholder} alt="person" width="350">
		<form on:submit={handleOnSubmit}>
			<Textfield bind:value={username} label="Username" />
	
			<Textfield bind:value={password} type="password" label="Password" />
	
			<Button variant="raised" type="submit"><Label>Login</Label></Button>
			<Button variant="outlined" type="submit"><Label>Signup</Label></Button>
			<p>Or</p>
			<Button variant="outlined" type="submit"><Label>Signup with Google</Label></Button>
			<Button variant="outlined" type="submit"><Label>Signup with Apple</Label></Button>
			<Button variant="outlined" type="submit"><Label>Signup with Facebook</Label></Button>
		</form>
	</div>
</main>

<style>
	.container {
		display:grid;
		gap: 2em;
		grid-template-columns: 1fr 2fr;

	}

	p {
		color: white;
		text-align: center;
	}

	form {
		display:grid; 
		width:max-content;
		gap: 20px;
		background: #000000bb;
		padding: 50px;
	}

	h2 {
		color: white;
		margin: 0.25em 0;
	}
</style>
