<script>
	let tasks = '';
	let tasks_array = [];

	const event_tasks = (e) => {
		// pull data from user input
		tasks = e.target.value;
	};

	const addtasks = (e) => {
		// this function should add tasks to the list dynamically
		tasks_array.push(tasks);
     tasks_array = tasks_array
	};

</script>


<!-- Steps 
1. EXPECTED: user types something in the input and event_tasks pulls the data ACTUAL: that's happening 
2. Expected: when user clicks the add task button, the item gets added to the list Actual; Item is not getting added to the list correctly
3. EXPECTED: item should display with index number and item as string actual only li tags are getting displayed and each letter is getting displayed 
4. expected: item should keep adding to the intial list acutual; list is changed everytime the button is clicked
-->

<main>
	<ul>
		{#each tasks_array as task, index}
			<li>{index + 1}:  {task}</li>
		{/each}
	</ul>
	<div>
		<div>Dummy Calendar data here</div>
		<h2>Tasks in relevance to the Calendar</h2>
	</div>
	<span>Today's Task<br /><input on:input={event_tasks} /></span>
	<br />
	<button on:click={addtasks}>Add Tasks</button>
</main>

<style>
   li{
     list-style-type: none;
   }
</style>
