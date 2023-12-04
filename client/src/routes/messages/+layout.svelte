<script>
	import logo from '$lib/icons/logo.svg';
	const links = [
		{ name: 'Dashboard', href: '/dashboard', image: 'dashboard.svg'},
		{ name: 'Calendar', href: '/calendar', image: 'calendar.svg' },
		{ name: 'Events', href: '/events', image: 'events.svg' },
		{ name: 'Tasks', href: '/tasks', image: 'tasks.svg' },
		{ name: 'Messages', href: '/messages', image: 'messages.svg' },
		{ name: 'Settings', href: '/settings', image: 'settings.svg' }
	];
</script>


<div id="menu">
	<h1><img alt="logo" src={logo} />EEA</h1>
	<nav>
		<ul>
			{#each links as { name, href, image }}
				<li>
					<a style="--bgImage: url(./icons/{image});" class="menu-link" {href}>{name}</a>
				</li>
			{/each}
		</ul>
	</nav>
</div>
<slot />
<div id="sidebar">
	<div id="button-holder">
		<a id="profile" href="#profile">Profile</a>
		<button id="logout-btn">Logout</button>
	</div>
	<div id="user-pic" />
	<div id="user-info">
		<div id="user-name">User's Name</div>
		<div id="user-status">Status</div>
	</div>
</div>

<style>
	#menu,
	#sidebar {
		background-color: #0000000d;
		min-height: 100vh;
	}
	#sidebar {
		padding: 20px;
		padding-top: 90px;
		min-width: 300px;
		text-align: center;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	#menu {
		padding: 32px 0 0 32px;
		min-width: 12em;
	}
	h1 {
		font-size: 16px;
		font-weight: bold;
		margin: 0;
		line-height: 1em;
		display: flex;
		align-items: center;
		gap: 9px;
	}
	h1 img {
		width: 35px;
		height: auto;
	}
	#user-pic {
		border-radius: 100%;
		width: 150px;
		height: 150px;
		background-color: orange;
		background-clip: content-box;
		padding: 0.5em;
		margin-right: 0px;
	}
	#user-name {
		font-weight: bold;
		padding: 0.5em;
	}
	#user-info {
		text-align: center;
	}
	nav {
		margin-top: 79px;
	}
	nav ul {
		padding: 0;
		list-style-type: none;
		display: flex;
		flex-flow: column;
		gap: 32px;
		align-items: flex-start;
	}
	nav a,
	#logout-btn,
	#profile {
		display: flex;
		align-items: center;
		text-decoration: none;
		color: inherit;
	}
	.menu-link {
		transition: background-color 0.2s;
		padding: 0.5em;
		border-radius: 14px;
	}
	.menu-link:hover {
		background-color: #0000001a;
		border: none;
	}

	nav a::before,
	#logout-btn::before {
		content: '';
		margin-right: 1em;
		width: 20px;
		height: 20px;
		background-repeat: no-repeat;
		background-image: var(--bgImage);
		background-size: contain;
		background-position: 50% 50%;
	}

	#button-holder {
		display: flex;
		gap: 8vw;
		align-items: center;
	}
	#button-holder > * {
		font-size: inherit;
		border: none;
		background: none;
		cursor: pointer;
	}
	#logout-btn::before {
		--bgImage: url('/icons/logout.svg');
		margin-right: 0.5em;
	}

	:global(body) {
		display: grid;
		grid-template-columns: auto 1fr auto;
	}
</style>
