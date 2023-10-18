<script>
	import Button, { Label } from '@smui/button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	import { Input } from '@smui/textfield';
	import placeholder2 from './assets/placeholder-login2.svg';
	import googleIcon from './assets/google-icon.svg';
	import appleIcon from './assets/apple-icon.svg';
	import facebookIcon from './assets/facebook-icon.svg';
	import logo from '$lib/icons/logo.svg';

	let usernameInput,
		passwordInput,
		username = '',
		password = '';
	$: console.log(username);
	$: console.log(password);

	// submit post request to backend login route
	const handleOnSubmit = async (event) => {
		event.preventDefault();
		console.log('submitting login information');
		//logic for submitting to backend server running FASTAPI on port 8000
		fetch('http://127.0.0.1:8000/token', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			body: new URLSearchParams({ username, password }).toString()
		})
			.then((response) => {
				if (!response.ok) {
					console.error(response.json);
					throw new Error('Network response was not ok');
				}
				return response.json();
			})
			.then((result) => {
				console.log(result);
			})
			.catch((error) => {
				console.log(`Error with the fetch operation: ${error}`);
			});
	};
</script>

<h1><img alt="logo" src={logo} />EEA</h1>

<main>
	<div class="container">
		<img class="illustration" src={placeholder2} alt="person" />
		<form on:submit={handleOnSubmit}>
			<div class="inner-flex">
				<label for="username">Email</label>

				<Textfield id="username" class="solo-input" variant="filled" bind:input={usernameInput}>
					<Input
						placeholder="Enter email address"
						bind:this={usernameInput}
						bind:value={username}
					/>
				</Textfield>
				<label for="password">Password</label>

				<Textfield id="password" class="solo-input" variant="filled" bind:input={passwordInput}>
					<Input
						type="password"
						placeholder="Enter password"
						bind:value={password}
						bind:this={passwordInput}
					/>
				</Textfield>
			</div>
			<Button variant="raised" type="submit"><Label>Login</Label></Button>
			<Button variant="raised" color="secondary" type="submit"><Label>Signup</Label></Button>
			<div class="or">Or</div>
			<Button variant="outlined" type="submit">
				<img src={googleIcon} class="brand-icon" alt="google icon" />
				<Label>Sign in with Google</Label></Button
			>
			<Button variant="outlined" type="submit">
				<img src={appleIcon} class="brand-icon" alt="apple icon" />
				<Label>Sign in with Apple</Label></Button
			>
			<Button variant="outlined" type="submit">
				<img src={facebookIcon} class="brand-icon" alt="facebook logo" />
				<Label>Sign in with Facebook</Label></Button
			>
		</form>
	</div>
</main>

<style>
	:global(body) {
		background-color: #f2f2f2;
	}
	h1 {
		font-size: 32px;
		font-weight: bold;
		margin: 49px 0 0 57px;
		line-height: 1em;
		display: flex;
		align-items: center;
		gap: 9px;
	}
	h1 img {
		width: 70px;
		height: auto;
	}
	main {
		margin: 100px;
	}

	.container {
		justify-content: space-between;
		display: flex;
		align-items: center;
	}

	.or {
		color: #0000009f;
		text-align: center;
	}

	form {
		display: flex;
		flex-flow: column;
		justify-content: center;
		gap: 38px;
		min-width: max-content;
		background-color: white;
		color: black;
		padding: 50px;
		border-radius: 14px;
	}

	.illustration {
		margin-left: 50px;
		height: auto;
		width: 502.92px;
		min-width: 0;
	}
	.brand-icon {
		width: 18px;
		height: auto;
		margin-right: 1em;
	}
	label {
		font-weight: bold;
	}
	.inner-flex {
		display: flex;
		flex-flow: column;
		gap: 1em;
	}
	:global(.solo-input::placeholder) {
		opacity: 1;
		color: #0000009f;
	}
</style>
