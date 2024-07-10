<script>
	import { getContext } from 'svelte';
	const i18n = getContext('i18n');
</script>

<div class="  text-center text-6xl mb-3">📄</div>
<div class="text-center  text-2xl font-semibold z-50">{$i18n.t('Add Files')}</div>

<slot
	><div class=" mt-2 text-center text-sm  w-full">
		{$i18n.t('Drop any files here to add to the conversation')}
	</div>
</slot>
