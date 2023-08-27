<script>
	import { Input } from '@smui/textfield';
	let searchValue = '';
</script>

<main>
	<div id="search">
		<Input class="solo-input" placeholder="Search" bind:value={searchValue} />
	</div>
	<h2>Dashboard</h2>
</main>

<style>
	main {
		padding: 32px;
	}
	#search {
		display: flex;
	}
	h2 {
		font-size: 1.5em;
		font-weight: 400;
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
