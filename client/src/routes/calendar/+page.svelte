<script>
	import { DateInput, DatePicker, localeFromDateFnsLocale } from 'date-picker-svelte'
	import { onMount } from 'svelte';

	let deg = 0;
	onMount(() => {
		const interval = setInterval(() => {
			deg += 2;
			if (deg >= 360) deg = 0;
			document.body.style.setProperty('--deg', deg);
		}, 60);
		return () => clearInterval(interval);
	});
</script>

<div>
	<DateInput
	format="yyyy/MM/dd HH:mm:ss"
	placeholder="2000/31/12 23:59:59" />
	<DatePicker />
</div>

<style>
	:global(body) {
		/* --date-picker-foreground: #f7f7f7;
		--date-picker-background: #16171c; */
		--date-picker-highlight-border: hsl(var(--deg), 98%, 49%);
		/* --date-picker-highlight-shadow: hsla(var(--deg), 98%, 49%, 50%);
		--date-picker-selected-color: hsl(var(--deg), 100%, 85%); */
		--date-picker-selected-background: hsla(var(--deg), 98%, 49%, 20%);
		/* background: #0d0e12; */
		color: #0a0909;
		transition: all 80ms ease-in-out;
		font-size: 14px;
	}
	div {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

</style>