<script>
	// handleSubmit
	const handleOnSubmit = (e) => {
		e.preventDefault();
		console.log('submitting  the data to the back end ');
	};

	// handle form input
	let First_name = '';
	let Last_name = '';
	let E_mail = '';
	let Pass_word = '';

	const handleInputfirstName = (e) => {
		First_name = e.target.value;
		console.log('F_name', First_name);
	};
	const handleInputlastName = (e) => {
		Last_name = e.target.value;
		console.log('L_name', Last_name);
	};
	const handleInputEmail = (e) => {
		E_mail = e.target.value;
		console.log('E_mail', E_mail);
	};
	const handleInputPassword = (e) => {
		Pass_word = e.target.value;
		console.log('P_word', Pass_word);
	};

	//  radio buttons
	let roles = ['Admin', 'Organizer', 'Volunteer'];
	let user_role = '';

</script>

<main>
	<h2>Register</h2>
	<form on:submit={handleOnSubmit}>
		<label
			>First Name:
			<input type="text" value={F_name} on:input={handleInputfirstName} required />
		</label>
		<label
			>Last Name:
			<input type="text" value={L_name} on:input={handleInputlastName} required />
		</label>
		<label
			>Email:
			<input type="text" value={E_mail} on:input={handleInputEmail} required />
		</label>
		<label
			>Password:
			<input type="text" value={P_word} on:input={handleInputPassword} required />
			<br />
			<button>Register</button>
		</label>
	</form>
	<div>Select Role:</div>
	{#each roles as role}
		<label>
			<div>{role}</div>
			<input type="radio" value="role" bind:group={user_role} />
		</label>
	{/each}
	</main>

<style>
	label {
		color: white;
	}

	h2,
	h5,
	div {
		color: white;
	}
</style>
