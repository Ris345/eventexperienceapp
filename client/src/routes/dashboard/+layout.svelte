<script>
	let logo = '../icons/logo.svg';
	let logout = '../icons/logout.svg'
	const links = [
		{ name: 'Dashboard', href: '#dashboard', image: 'dashboard.svg' },
		{ name: 'Calendar', href: '#calendar', image: 'calendar.svg' },
		{ name: 'Events', href: '#events', image: 'events.svg' },
		{ name: 'Tasks', href: '#tasks', image: 'tasks.svg' },
		{ name: 'Messages', href: '#messages', image: 'messages.svg' },
		{ name: 'Settings', href: '#settings', image: 'settings.svg' }
	];
</script>

<div id="menu">
	<h1><img alt="logo" src={logo} />EEA</h1>
	<nav>
		<ul>
			{#each links as { name, href, image }}
				<li>
					<a style="--bgImage: url(./icons/{image});" id="menu-link" {href}>{name}</a>
				</li>
			{/each}
		</ul>
	</nav>
</div>
<slot />
<div id="sidebar">
	<div id="button-holder">
		<button type="button">Profile</button>
		<a href='#logout' id='logout-link'><img alt="logout" src={logout} id="logout-img"/>Logout</a>
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
		margin-top: 40px;
		margin-bottom: 30px;
		margin-right: 0px;
		
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
	}
	nav a, 
	#logout-link {
		display: flex;
		align-items: center;
		text-decoration: none;
		color: inherit;
	}

	#menu-link:hover {
		background-color: rgb(184, 184, 184);
		border:none;
		border-radius:10px;
		padding-left: 7px;
	}

	nav a::before {
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

	#logout-img {
		margin-right: 3px;
	}

	:global(body) {
		display: grid;
		grid-template-columns: auto 1fr auto;
	}
</style>
