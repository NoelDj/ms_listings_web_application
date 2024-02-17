<script lang="ts">
    export let informationSet
    export let baseImagePath
    import { page } from '$app/stores';
    const beta = $page.url.searchParams.get('page') || 1

  
    const listings = informationSet.results.listings
    const { count } = informationSet
    const imageExists = (images) => images && images.length > 0
    const amount = informationSet.results.amount
    const showPagination = count > amount
    
    const lastPage = Math.ceil(informationSet.count / amount)
    let currentPage = parseInt(beta)
    
    
    
    const hasPreviousPage = informationSet.previous && informationSet.previous.includes('page=')
    const previousPage = hasPreviousPage ? parseInt(informationSet.previous.match(/page=(\d+)/)?.[1] || '', 10) : ''
    
    const nextPage = informationSet.next ? parseInt(informationSet.next.match(/page=(\d+)/)[1]) : ''
    
    const pageNumbers = pagination(currentPage,lastPage)

    let linkUrl = ''

    $page.url.searchParams.forEach((value, key) => {
        if (key !== 'page') {
          linkUrl += `&${key}=${value}`
        }
    })

    const pagination = (c:number, m:number): Array<string | number> => {
      var current = c,
      last = m,
      delta = 2,
      left = current - delta,
      right = current + delta + 1,
      range: Array<number> = [],
        rangeWithDots: Array<string | number> = [],
      l;
      
      for (let i = 1; i <= last; i++) {
        if (i == 1 || i == last || i >= left && i < right) {
          range.push(i);
        }
      }
      
      for (let i of range) {
        if (l) {
          if (i - l === 2) {
            rangeWithDots.push(l + 1);
          } else if (i - l !== 1) {
            rangeWithDots.push('...');
          }
        }
        rangeWithDots.push(i);
        l = i;
      }
      
      return rangeWithDots;
    }

  </script>
 
  <div class="grid grid-cols-[repeat(auto-fit,minmax(350px,1fr))] gap-5">
    {#each listings as listing}
      <div class="max-w-sm rounded overflow-hidden shadow-lg">
        {#if imageExists(listing.images)}
          <img class="w-full" src="{baseImagePath + listing.images[0].src}" style="height: 200px;object-fit: cover;" alt="{listing.title} image">
        {:else}
          <img class="w-full" src="/tower.PNG" alt="{listing.title} image">
        {/if}
        <div class="px-6 py-4">
          <div class="font-bold text-xl mb-2">
            <a href="{`/listing/${listing.id}`}">{listing.title}</a>
          </div>
        </div>
        <div class="px-6 pt-4 pb-2">
          <span class="inline-flex items-center rounded-md bg-indigo-50 px-2 py-1 text-xs font-medium text-indigo-700 ring-1 ring-inset ring-indigo-700/10">
            <a href="{`/category/${listing.category.name}`}">{listing.category.name}</a>
          </span>
          <span class="inline-flex items-center rounded-md bg-indigo-50 px-2 py-1 text-xs font-medium text-indigo-700 ring-1 ring-inset ring-indigo-700/10">
            <a href="{`/user/${listing.owner.username}`}">{listing.owner.username}</a>
          </span>
        </div>
      </div>
    {/each}
  </div>
  {#if showPagination}
  <div class="flex items-center justify-between border-t border-gray-200 bg-white px-4 py-3 sm:px-6">
    <div class="flex flex-1 justify-between sm:hidden">
      <a href="{`?page=${previousPage}`}" class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Previous</a>
      <a href="{`?page=${nextPage}`}" class="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">Next</a>
    </div>
    <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
      <div>
        <p class="text-sm text-gray-700">
          Showing
          <span class="font-medium">{(currentPage * amount) - amount + 1}</span>
          to
          <span class="font-medium">{currentPage * amount}</span>
          of
          <span class="font-medium">{count}</span>
          results
        </p>
      </div>
      <div>
        <nav class="isolate inline-flex -space-x-px rounded-md shadow-sm" aria-label="Pagination">
          
          {#if currentPage !== 1}
          <a data-sveltekit-reload href="{`?page=${previousPage}`}" class="relative inline-flex items-center rounded-l-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0">
            <span class="sr-only">Previous</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd" d="M12.79 5.23a.75.75 0 01-.02 1.06L8.832 10l3.938 3.71a.75.75 0 11-1.04 1.08l-4.5-4.25a.75.75 0 010-1.08l4.5-4.25a.75.75 0 011.06.02z" clip-rule="evenodd" />
            </svg>
          </a>
          {/if}
  
          {#each pageNumbers as pageNumber}
            {#if pageNumber == '...'}
              <span class="relative inline-flex items-center px-4 py-2 text-sm font-semibold select-none text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:outline-offset-0">...</span>
            {:else}
              <a data-sveltekit-reload href="{`?page=${pageNumber}${linkUrl}`}" class="relative inline-flex items-center px-4 py-2 text-sm font-semibold {pageNumber === currentPage ? 'bg-indigo-600 text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600' : 'text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:outline-offset-0'}">
                {pageNumber}
              </a>
            {/if}
          {/each}
          
          {#if currentPage !==lastPage}
          <a data-sveltekit-reload href="{`?page=${nextPage}`}" class="relative inline-flex items-center rounded-r-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0">
            <span class="sr-only">Next</span>
            <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z" clip-rule="evenodd" />
            </svg>
          </a>
          {/if}
        </nav>
      </div>
    </div>
  </div>
  {/if}
  