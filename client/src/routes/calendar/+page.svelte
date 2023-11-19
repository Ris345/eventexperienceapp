<script>
	import { Input } from '@smui/textfield';
	import todayDate from '$lib/todayDate.js';
	let searchValue = '';
	const currentDate = new Date();
	let calendar = 'calendar page  '
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
	<div>Hello {calendar}</div>
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
