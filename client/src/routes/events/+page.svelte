<script>
	import { Input } from '@smui/textfield';
	import todayDate from '$lib/todayDate.js';
	let searchValue = '';
	let eventName = ''
	let eventDate = ''
	let startTime = ''
	let endTime =  ''
	let location = ''
	let organizer = ''
	let eventDescription = ''
	let rsvp = null; 

	const currentDate = new Date();
	let events = 'Events Page'

	$: console.log('eventName:', eventName);
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
	<div>
		<form method="POST">
			<label>
				EventName:
				<input name="eventName" type="text" bind:value={eventName} >
			</label>
			<label>
				EventDate:
				<input name="date" type="date" bind:value={eventDate} >
			</label>
			<label>
				Start Time:
				<input name="time" type="time" bind:value={startTime} >
			</label>
			<label>
				End Time:
				<input name="time" type="time" bind:value={endTime} >
			</label>
			<label>
				Location: 
				<input name="location" type="text" bind:value={location} >
			</label>
			<label>
				Organizer:
				<input name="text" type="text" bind:value={organizer} >
			</label>
			<label>
				Event Description: 
				<input name="text" type="text" bind:value={eventDescription} >
			</label>
			<label>
			    RSVP:
				<input name="password" type="password" bind:value={rsvp} >
				<select name="studentAns" id="studentAns">
					<option value="-">Not Sure</option>
					<option value="Yes">Yes</option>
					<option value="No">No</option>
				  </select>
			</label>
			<button>Enter Event Details</button>
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
