<script>
	import Button, { Label } from '@smui/button';
	import Paper, { Title, Content } from '@smui/paper';
	import Dialog, { Title as DTitle, Content as DContent, Actions } from '@smui/dialog';
	import { fly } from 'svelte/transition';
	import { onMount } from "svelte";


	class Meetup {
		constructor(date, duration = 3, attendees = []) {
			this.date = date;
			this.duration = duration;
			this.attendees = attendees;
		}
	}
	let notifications = [];
	export let events = [];
	let open = false,
		selectedEvent = null;
	function populate() {
		events = [];
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
		// remove notifications from display
		notifications = [];
}
	
	
  class Notification {
		constructor(type, date, user, meetup, content) {
				this.type = type;
				this.date = date;
				this.user = user;
				this.meetup = meetup;
				this.content = content;
			}
	}
	
	function getNotifications () {
		notifications = [];
		const notification = new Notification(
			"event",
			"NewAlert",
			"username 123",
			"Meetup On AI and Robots",
			"This is the content of the notification."
		);
		notifications.push(notification);
		//remove events from display
		events = [];

		console.log(notifications);
	}


</script>

<main>
	<!-- Causes runtime error currently -->
	<Dialog bind:open>
		<DTitle>Confirm your RSVP</DTitle>
		<DContent>
			Will you be attending on {selectedEvent && selectedEvent.date.toLocaleDateString()}?
		</DContent>
		<Actions>
			<Button on:click={() => (open = false)}><Label>Yes</Label></Button>
			<Button on:click={() => (open = false)}><Label>No</Label></Button>
		</Actions>
	</Dialog>
	<h2>Upcoming Events</h2>
	<div id='notificationsButton'>
		<Button type="button" on:click={getNotifications} variant="raised">
			<Label>Notifications</Label>
		</Button>
	</div>
	<div id="calendar">
		{#each notifications as notification, i (notification.type)}
			<div in:fly={{ x: 100, delay: i * 150 }}>
				<Paper color="primary">
					<Title>{notification.content}</Title>
					<Content>
						<div>
							"hello"
						</div>
					</Content>
				</Paper>
			</div>
		{/each}
		{#each events as event, i (event.date)}
			<div in:fly={{ x: 100, delay: i * 150 }}>
				<Paper color="primary">
					<Title>{event.date.toLocaleDateString()}</Title>
					<Content>
						<div class="time">
							{event.date.toLocaleTimeString().split(':')[0] +
								event.date.toLocaleTimeString().split(' ')[1]}
						</div>
						<Button
							color="secondary"
							variant="raised"
							on:click={() => {
								selectedEvent = event;
								open = true;
							}}><Label>RSVP</Label></Button
						>
						Attendees: {event.attendees}
					</Content>
				</Paper>
			</div>
		{/each}
		{#if events.length === 0}
			<div id="fallback">No upcoming events found</div>
		{/if}
	</div>
	<Button type="button" on:click={populate} variant="raised"
		><Label>Populate Events (TESTING ONLY)</Label></Button>
	
	
		
	
	
	
	
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
		overflow: hidden;
	}

	#notification {
		border: 1px solid black;
		background: white;
		margin: 0 5px 1em 5px;
		display: flex;
		flex-flow: column;
		gap: 0.5em;
		padding: 0.5em;
		overflow: hidden;
	}

	.time {
		margin-bottom: 0.5em;
	}
	#fallback {
		font-size: 1.2em;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 200px;
	}
	#notificationsButton {
	margin-bottom: 10px;	
	margin-right: 10px;
	display: flex;
	justify-content: right;
	}


</style>
