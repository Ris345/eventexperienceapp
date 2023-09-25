<script>
    import Button from '@smui/button';

    import Form from './Form.svelte'
    import profile_icon from "./assets/profile_icon.jpg"


    let toggle = false;

    function toggleProfile() {
        toggle = !toggle
    }

</script>

<div class="container">
    <h2>
        Welcome User
    </h2>
    <div>
        <img src={profile_icon} alt="profile_image">
    </div>

    <Button on:click={toggleProfile} variant="raised">Edit profile</Button>
        
    {#if toggle}
       <div>
            <Form />
            <Button on:click={toggleProfile} variant="raised">Save</Button>
        </div>
    {/if}
    
</div>

<style>

	h2 {
		color: white;
		margin: 0.25em 0;
	}

    img {
        flex: auto;
    }


</style>


