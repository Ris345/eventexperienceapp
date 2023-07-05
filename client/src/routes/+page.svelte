<script>
	export let events = [];
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
</main>

<style>
	h2 {
		color: white;
		margin: 0.25em 0;
	}
	#calendar {
		border: 1px solid black;
		background: white;
	}
	#fallback {
		font-size: 1.2em;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 200px;
	}
</style>
