
<script>
    import Calendar from '@event-calendar/core';
    import TimeGrid from '@event-calendar/time-grid';
	import '@event-calendar/core/index.css';

    let plugins = [TimeGrid];
    let options = {
        view: 'timeGridWeek',
        events: [
            // your list of events
        ]
    };

	function updateOptions() {
        options.slotDuration = '01:00';
    }
	
</script>

<button on:click={updateOptions}>Change slot duration</button>
<Calendar {plugins} {options} />


