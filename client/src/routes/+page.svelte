<script>
	import Button, { Label } from '@smui/button';
	import Paper, { Title, Content } from '@smui/paper';
	import { fly } from 'svelte/transition';
	class Meetup {
		constructor(date, duration = 3, attendees = []) {
			this.date = date;
			this.duration = duration;
			this.attendees = attendees;
		}
	}
	export let events = [];
	function populate() {
		for (let i = 0; i < 3; i++) {
			const date = new Date(
				2023,
				Math.floor(Math.random() * 12),
				Math.floor(Math.random() * 28) + 1,
				14
			);
			events.push(new Meetup(date));
		}
		events = events;
	}
</script>

<main>
	<h2>Upcoming Events</h2>
	<div id="calendar">
		{#if events.length > 0}
			{#each events as event (event.date)}
				<div in:fly={{ x: -100 }}>
					<Paper color="primary">
						<Title>{event.date.toLocaleDateString()}</Title>
						<Content>
							{event.date.toLocaleTimeString().split(':')[0] +
								event.date.toLocaleTimeString().split(' ')[1]}
						</Content>
					</Paper>
				</div>
			{/each}
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
		display: flex;
		flex-flow: column;
		gap: 0.5em;
		padding: 0.5em;
	}

	#fallback {
		font-size: 1.2em;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 200px;
	}
</style>
