<script>
	import { Input } from '@smui/textfield';
	import todayDate from '$lib/todayDate.js';
	import { createEventDispatcher } from 'svelte';
	import axios from 'axios';
	let searchValue = '';
	let eventName = '';
	let eventDate = '';
	let startTime = '';
	let endTime = '';
	let location = '';
	let organizer = '';
	let eventDescription = '';
	let rsvp = null;

	const currentDate = new Date();
	let events = 'Events Page';
	const dispatch = createEventDispatcher();
	// handleSubmit
	const handleOnSubmit = async (e) => {
		e.preventDefault();
		console.log('submitting  the data to the back end ');
		$: console.log('eventName:', eventName);
		$: console.log('eventDate:', eventDate);
		$: console.log('startTime:', startTime);
		$: console.log('endTime:', endTime);
		$: console.log('location:', location);
		$: console.log('organizer:', organizer);
		$: console.log('eventDescription:', eventDescription);
		$: console.log('rspv:', rsvp);
		// make a post request
		try {
			const response = await axios.post('/events', {
				eventName,
				eventDate,
				startTime,
				endTime,
				location,
				organizer,
				eventDescription,
				rsvp
			});
			dispatch('formSubmitted', response.data);
		} catch (error) {
			console.error(error);
		}
	};
</script>

<main>
	<div id="search">
		<Input class="solo-input" placeholder="Search" bind:value={searchValue} />
	</div>
	<div id="header-bar">
		<div id="date">
			{todayDate}
		</div>
	</div>
	<div class="formComponent">
		<form on:submit={handleOnSubmit} class="formInner">
			<div class="formRow">
				<label for="eventName">Task Name:</label>
				<input id="eventName" name="eventName" type="text" bind:value={eventName} />
			</div>
			<div class="formRow">
				<label for="date">Quantity:</label>
				<input id="date" type="number" bind:value={eventDate} />
			</div>
			<div class="formRow">
				<label for="startTime">Assigned User:</label>
				<input id="startTime" name="startTime" type="text" bind:value={startTime} />
			</div>
			<div class="formRow">
				<label for="endTime"> Date Created:</label>
				<input id="endTime" name="endTime" type="date" bind:value={endTime} />
			</div>
			<div class="formRow">
				<label for="location"> Date Updated:</label>
				<input id="location" name="location" type="date" bind:value={location} />
			</div>
			<div class="formRow">
				<label for="rsvp">Complete</label>
				<select id="rsvp" name="studentAns" bind:value={rsvp}>
					<option value="-">Delayed</option>
					<option value="Yes">Yes</option>
					<option value="No">No</option>
				</select>
			</div>
			<div class="formRow">
				<label for="eventDescription"> Task Description:</label>
				<input
					id="eventDescription"
					name="eventDescription"
					type="text"
					bind:value={eventDescription}
				/>
			</div>
			<div class="button">
				<button>Enter Task Details</button>
			</div>
		</form>
	</div>
</main>

<style>
	main {
		padding: 32px;
	}
	#search {
		display: flex;
		margin-bottom: 31px;
	}
	#header-bar {
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 1rem;
	}
	h2 {
		font-weight: 400;
		font-size: inherit;
		line-height: 1rem;
		margin: 0;
	}
	#date {
		color: #00000080;
	}

	.formComponent {
		display: flex;
		justify-content: center; /* Center the form horizontally */
		align-items: center; /* Center the form vertically */
		height: 100vh; /* Adjust the height as needed */
	}

	.formInner {
		width: 400px; /* Set the width of the form */
		padding: 20px;
		border: 1px solid #797979;
	}

	.formRow {
		display: flex;
		flex-direction: column;
		margin-bottom: 10px;
	}

	label {
		margin-bottom: 5px;
	}

	.button {
		display: flex;
		flex-direction: column;
		margin-bottom: 10px;
		border-radius: 45%;
	}

	:global(.solo-input) {
		width: 100%;
		border: 1.5px solid #00000040;
		border-radius: 100px;
		background-image: url('./icons/search.svg');
		background-repeat: no-repeat;
		background-size: 20px;
		background-position: 0.5em 50%;
		padding: 1em 0.5em;
		padding-left: calc(1em + 20px);
	}
	:global(.solo-input::placeholder) {
		opacity: 1;
		color: #00000040;
	}
</style>
