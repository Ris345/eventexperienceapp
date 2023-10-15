const currentDate = new Date(),
    todayDate = currentDate.toLocaleDateString('en-US', {
        weekday: 'long',
        month: 'long',
        year: 'numeric',
        day: 'numeric'
    });
export default todayDate;