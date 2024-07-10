<script lang="ts">
	import { createEventDispatcher, tick } from 'svelte';
	import { Switch } from 'bits-ui';
	export let state = true;

	const dispatch = createEventDispatcher();
</script>

<Switch.Root
	bind:checked={state}
	onCheckedChange={async (e) => {
		await tick();
		dispatch('change', e);
	}}
	class="flex h-5 min-h-5 w-9 shrink-0 cursor-pointer items-center rounded-full px-[3px] transition  {state
		? ' bg-primary-dark '
		: 'bg-gray-200 '} outline outline-1 outline-gray-100 "
>
	<Switch.Thumb
		class="pointer-events-none block size-4 shrink-0 rounded-full bg-white transition-transform data-[state=checked]:translate-x-3.5 data-[state=unchecked]:translate-x-0 data-[state=unchecked]:shadow-mini "
	/>
</Switch.Root>
