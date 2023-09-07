<script>
	import Button, { Label } from '@smui/button';
	import Textfield from '@smui/textfield';
	import HelperText from '@smui/textfield/helper-text';
	import { Input } from '@smui/textfield';
	import { createEventDispatcher } from 'svelte';
	import axios from 'axios';
	// import placeholder from "./assets/placeholder-login.jpeg"
	import placeholder2 from "./assets/placeholder-login2.svg"


	let username = '',
		password = '';
	$: console.log(username);
	$: console.log(password);
	const dispatch = createEventDispatcher();

	export let size = "1em";
	export let width = size;
	export let height = size;
	export let color = "currentColor";
	export let viewBox = "0 0 24 24";
	export let ariaLabel = void 0;
	export let ariaHidden = void 0;
	export let title = void 0;
	export let desc = void 0;

	let className = void 0;
	export { className as class }

	const handleOnSubmit = async (e) => {
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
	<div class="container">
		
		<img src={placeholder2} alt="person">
		<form on:submit={handleOnSubmit}>
			<Input class="solo-input" placeholder="Username" bind:value={username} />
			<Input class="solo-input" bind:value={password} type="password" label="Password" placeholder="Password" />
	
			<Button variant="raised" type="submit"><Label>Login</Label></Button>
			<Button variant="raised" color ='secondary' type="submit"><Label>Signup</Label></Button>
			<p>Or</p>
			<Button variant="outlined" type="submit"><svg viewBox="{viewBox}" width="{width}" height="{height}" class="{className}" aria-label="{ariaLabel}" aria-hidden="{ariaHidden}">{#if desc}<desc>{desc}</desc>{/if}{#if title}<title>{title}</title>{/if}<path d="M21.35,11.1H12.18V13.83H18.69C18.36,17.64 15.19,19.27 12.19,19.27C8.36,19.27 5,16.25 5,12C5,7.9 8.2,4.73 12.2,4.73C15.29,4.73 17.1,6.7 17.1,6.7L19,4.72C19,4.72 16.56,2 12.1,2C6.42,2 2.03,6.8 2.03,12C2.03,17.05 6.16,22 12.25,22C17.6,22 21.5,18.33 21.5,12.91C21.5,11.76 21.35,11.1 21.35,11.1V11.1Z" fill="{color}"/></svg>
				<Label>Signup with Google</Label></Button>
			<Button variant="outlined" type="submit"><svg viewBox="{viewBox}" width="1.4em" height="1.4em" class="{className}" aria-label="{ariaLabel}" aria-hidden="{ariaHidden}">{#if desc}<desc>{desc}</desc>{/if}{#if title}<title>{title}</title>{/if}<path d="M18.71,19.5C17.88,20.74 17,21.95 15.66,21.97C14.32,22 13.89,21.18 12.37,21.18C10.84,21.18 10.37,21.95 9.1,22C7.79,22.05 6.8,20.68 5.96,19.47C4.25,17 2.94,12.45 4.7,9.39C5.57,7.87 7.13,6.91 8.82,6.88C10.1,6.86 11.32,7.75 12.11,7.75C12.89,7.75 14.37,6.68 15.92,6.84C16.57,6.87 18.39,7.1 19.56,8.82C19.47,8.88 17.39,10.1 17.41,12.63C17.44,15.65 20.06,16.66 20.09,16.67C20.06,16.74 19.67,18.11 18.71,19.5M13,3.5C13.73,2.67 14.94,2.04 15.94,2C16.07,3.17 15.6,4.35 14.9,5.19C14.21,6.04 13.07,6.7 11.95,6.61C11.8,5.46 12.36,4.26 13,3.5Z" fill="{color}"/></svg>
				<Label>Signup with Apple</Label></Button>
			<Button variant="outlined" type="submit"><svg viewBox="{viewBox}" width="{width}" height="{height}" class="{className}" aria-label="{ariaLabel}" aria-hidden="{ariaHidden}">{#if desc}<desc>{desc}</desc>{/if}{#if title}<title>{title}</title>{/if}<path d="M12 2.04C6.5 2.04 2 6.53 2 12.06C2 17.06 5.66 21.21 10.44 21.96V14.96H7.9V12.06H10.44V9.85C10.44 7.34 11.93 5.96 14.22 5.96C15.31 5.96 16.45 6.15 16.45 6.15V8.62H15.19C13.95 8.62 13.56 9.39 13.56 10.18V12.06H16.34L15.89 14.96H13.56V21.96A10 10 0 0 0 22 12.06C22 6.53 17.5 2.04 12 2.04Z" fill="{color}"/></svg>
				<Label>Signup with Facebook</Label></Button>
		</form>
	</div>
</main>

<style>


	:global(body) {
		background-color: #F2F2F2;
	}

	.container {
		justify-content: center;
		display: flex;
		align-items: center;
	}

	p {
		color: #0000009f;
		text-align: center;
	}

	form {
		display: grid; 
		width: max-content;
		gap: 20px;
		background-color: white;
		color: black;
		padding: 50px;
		margin: 2.5%;
		margin-left: 20%;
		border-radius: 20px;
		margin-top: 3%;
	}

	img {
		margin-top: 0;
		margin: 2.5%;
		width: 30%;
	}

	:global(.solo-input::placeholder) {
		opacity: 1;
		color: #0000009f;
	}	

	svg {
		margin-right: 10px;
	}

</style>
