<script>
	import logo from '$lib/icons/logo.svg';
</script>

<div id="menu">
	<h1><img alt="logo" src={logo} /> EEA</h1>
	<nav>
		<ul>
			<li>Dashboard</li>
			<li>Calendar</li>
			<li>Events</li>
			<li>Tasks</li>
			<li>Messages</li>
			<li>Settings</li>
		</ul>
	</nav>
</div>
<slot />
<div id="sidebar">
	<div id="button-holder">
		<button type="button">Profile</button>
		<button type="button">Logout</button>
	</div>
	<div id="user-pic" />
	<div id="user-name">User's Name</div>
	<div id="user-status">Status</div>
</div>

<style>
	#menu,
	#sidebar {
		background-color: #0000000d;
		padding: 20px;
	}
	h1 {
		font-size: 1.1rem;
		font-weight: bold;
		margin: 0;
		line-height: 1em;
		display: flex;
		align-items: center;
		gap: 9px;
	}
	#user-pic {
		border-radius: 100%;
		width: 150px;
		height: 150px;
		background-color: orange;
	}
	nav ul {
		list-style-type: none;
		padding: 0;
	}
	:global(body) {
		display: grid;
		grid-template-columns: auto 1fr auto;
	}
</style>
