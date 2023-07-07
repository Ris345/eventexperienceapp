<script>
	import Button, { Label } from '@smui/button';
	export let events = [];
	function populate() {}
</script>

<main>
	<h2>Upcoming Events</h2>
	<div id="calendar">
		{#if events.length > 0}
			<!--show each event as clickable tile-->
		{:else}
			<div id="fallback">No upcoming events found</div>
		{/if}
	</div>
	<Button type="button" on:click={populate} variant="raised"
		><Label>Populate Events (TESTING ONLY)</Label></Button
	>
</main>

<style>
	h2 {
		color: white;
		margin: 0.25em 0;
	}
	#calendar {
		border: 1px solid black;
		background: white;
		margin: 0 5px 1em 5px;
	}
	#fallback {
		font-size: 1.2em;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 200px;
	}
</style>
