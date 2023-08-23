<h1>
	<svg
		xmlns="http://www.w3.org/2000/svg"
		width="16"
		height="16"
		fill="currentColor"
		class="bi bi-door-open"
		viewBox="0 0 16 16"
	>
		<path d="M8.5 10c-.276 0-.5-.448-.5-1s.224-1 .5-1 .5.448.5 1-.224 1-.5 1z" />
		<path
			d="M10.828.122A.5.5 0 0 1 11 .5V1h.5A1.5 1.5 0 0 1 13 2.5V15h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V1.5a.5.5 0 0 1 .43-.495l7-1a.5.5 0 0 1 .398.117zM11.5 2H11v13h1V2.5a.5.5 0 0 0-.5-.5zM4 1.934V15h6V1.077l-6 .857z"
		/>
	</svg>
	BACKSTAGE
	<br />
	<span style="font-size:.5em; font-weight:300;">Event Experience Team Coordination</span>
</h1>
<slot />

<style>
	h1 {
		color: white;
		margin-top: 0.2em;
		line-height: 0.8em;
		font-size: 4em;
		font-weight: normal;
	}
	h1 svg {
		height: 1em;
		width: auto;
	}
	:global(body) {
		background-color: black;
		background-image: linear-gradient(to bottom, #000000aa, #000000aa),
			url('/images/backstage-horizontal.jpg');
		background-repeat: no-repeat;
		background-size: cover;
		height: 100%;
	}
	:global(html) {
		min-height: 100vh;
	}
</style>
