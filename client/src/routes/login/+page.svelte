<script>
	let username = '';
     const handleInputUsername = (e) => {
		username = e.target.value
		console.log('username',  username)
	 }

     let password = ''
	 const handleInputPassword = () => {
		password = ''
		console.log( 'password', password)
	 }

	 const handleOnSubmit = () => {
		console.log('subbmitting login information')
	 }
</script>


<main>
    <h2>Login</h2>
	<form on:submit={handleOnSubmit}>
		<label>Username
			<input type="text" value={username} on:input={handleInputUsername}/>
		</label>
		<label>Password
			<input type="password" value={password} on:input={handleInputPassword}/>
		</label>
        <br/>
		<button>Login</button>
	</form>

</main>

<style>
   label{
	color:white
   }

   h2{
	color: white;
   }

</style>