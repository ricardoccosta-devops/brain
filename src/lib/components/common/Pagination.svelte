<script lang="ts">
	import { Pagination } from 'bits-ui';
	import { createEventDispatcher } from 'svelte';

	import ChevronLeft from '../icons/ChevronLeft.svelte';
	import ChevronRight from '../icons/ChevronRight.svelte';

	export let page = 0;
	export let count = 0;
	export let perPage = 20;
</script>

<div class="flex justify-center">
	<Pagination.Root bind:page {count} {perPage} let:pages>
		<div class="my-2 flex items-center">
			<Pagination.PrevButton
				class="mr-[25px] inline-flex size-8 items-center justify-center rounded-[9px] bg-transparent hover:bg-primary-light  active:scale-98 disabled:cursor-not-allowed disabled:text-gray-400  hover:disabled:bg-transparent"
			>
				<ChevronLeft className="size-4" strokeWidth="2" />
			</Pagination.PrevButton>
			<div class="flex items-center gap-2.5">
				{#each pages as page (page.key)}
					{#if page.type === 'ellipsis'}
						<div class="text-sm font-medium text-foreground-alt">...</div>
					{:else}
						<Pagination.Page
							{page}
							class="inline-flex size-8 items-center justify-center rounded-[9px] bg-transparent hover:bg-primary-light  text-sm font-medium hover:bg-dark-10 active:scale-98 disabled:cursor-not-allowed disabled:opacity-50 hover:disabled:bg-transparent data-[selected]:bg-primary-dark data-[selected]:text-gray-100 data-[selected]:hover:bg-primary-dark"
						>
							{page.value}
						</Pagination.Page>
					{/if}
				{/each}
			</div>
			<Pagination.NextButton
				class="ml-[25px]  inline-flex size-8 items-center justify-center rounded-[9px] bg-transparent hover:bg-primary-light  active:scale-98 disabled:cursor-not-allowed disabled:text-gray-400  hover:disabled:bg-transparent"
			>
				<ChevronRight className="size-4" strokeWidth="2" />
			</Pagination.NextButton>
		</div>
	</Pagination.Root>
</div>
