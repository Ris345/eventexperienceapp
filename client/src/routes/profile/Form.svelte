<script>
    import Textfield from '@smui/textfield';

    let firstName = '',
        lastName = '',
        email = '',
        password = ''
</script>

<form action="profile">
    <Textfield bind:value={firstName} type="text" label="First Name"/>
    <Textfield bind:value={lastName} type="text" label="LastName"/>
    <Textfield bind:value={email} type="email" label="Email"/>
    <Textfield bind:value={password} type="password" label="Password"/>
</form>

<style>
    form {
        display:  grid;
        width: max-content;
        justify-items: center;
        padding-top: 5px;
        padding-bottom: 15px;
    }
</style>