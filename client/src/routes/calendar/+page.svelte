<script>
    import Calendar from '@event-calendar/core';
    import TimeGrid from '@event-calendar/time-grid';
    import DayGrid from '@event-calendar/day-grid'; 
    import '@event-calendar/core/index.css';

    let plugins = [TimeGrid, DayGrid];
    let options = {
        view: 'timeGridWeek',
        events: [
            // your list of events
        ],
        headerToolbar: {
            start: 'prev,next ', // Add navigation buttons
            center: 'title', // Display the title (date range)
            end: 'timeGridWeek,timeGridDay,dayGridMonth' // Add buttons for week and day views
        }
    };
</script>

<Calendar bind:plugins bind:options />
