<script>
	import Menu from '@smui/menu';
	import Button, { Label } from '@smui/button';
	import List, { Item, Separator, Text } from '@smui/list';
  	import { Anchor } from '@smui/menu-surface';

  let menu;


</script>

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

<!-- Notifications menu using SMUI https://sveltematerialui.com/demo/menu/ -->
<!-- currently not working -->
<div class='notifications' style="min-width: 100px;">
	<Button on:click={() => {
		menu.setOpen(true);
		console.log(menu);
	}}>
	  <Label>Notifications</Label>
	</Button>
	<Menu bind:this={menu}>
		<List>
			<Item on:SMUI:action={() => (console.log("clicked"))}>
				<Text style='color:black;'>Insert Item</Text>
			</Item>
		</List>
	</Menu>
</div>

<!-- Bell icon for notifications?
<div>
	<h2>
		<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
			 width="40" height="40.1" viewBox="0 0 1248.000000 1280.000000"
			 preserveAspectRatio="xMidYMid meet">
			<g transform="translate(0.000000,1280.000000) scale(0.100000,-0.100000)"
			fill="#000000" stroke="none">
			<path d="M6149 12782 c-298 -99 -505 -551 -549 -1197 -5 -82 -10 -162 -10
			-177 0 -28 -1 -28 -65 -28 -252 0 -632 -77 -920 -185 -518 -195 -987 -573
			-1341 -1081 -263 -377 -487 -880 -609 -1364 -70 -278 -94 -434 -125 -810 -173
			-2091 -419 -3500 -765 -4391 -147 -377 -377 -728 -585 -892 -241 -190 -449
			-256 -928 -296 -133 -11 -173 -31 -219 -108 -24 -42 -28 -58 -28 -128 0 -63 5
			-89 22 -121 29 -54 84 -101 130 -111 50 -10 12116 -10 12166 0 46 10 101 57
			130 111 17 32 22 58 22 121 0 70 -4 86 -28 128 -44 75 -86 96 -208 108 -372
			34 -510 65 -690 154 -120 59 -200 116 -303 215 -245 235 -432 569 -611 1091
			-297 863 -531 2305 -690 4249 -30 366 -66 579 -145 850 -231 799 -674 1477
			-1245 1905 -437 327 -981 522 -1536 551 l-126 7 -7 151 c-22 455 -107 789
			-260 1019 -132 200 -309 284 -477 229z"/>
			<path d="M5000 1593 c-6 -21 -17 -81 -25 -133 -83 -535 213 -1092 705 -1327
			137 -65 239 -97 385 -118 382 -56 776 72 1058 344 319 307 458 753 369 1181
			l-18 85 -1231 3 -1232 2 -11 -37z"/>
			</g>
			</svg>
			
	</h2>
</div> -->

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
	/* h2 {
		text-align: right;
		margin-top: 0px;
		margin-bottom: 0px;
		margin-right: 3%;
		padding-left: 10px;
		padding-right: 10px;
		float: right;
		background-color: rgb(255, 81, 0);
	} */
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
	.notifications {
		position: absolute;
		right: 5em;
		margin-top: 20px;
		font-weight: bolder;
		transform: scale(1.5);
	}
</style>
