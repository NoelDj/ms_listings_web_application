<script>
    import "../app.css";
    export let data;

</script>

{#if !data.isExpired}
    <header class="container mx-auto p-4 mb-3 shadow">
        <nav class="flex gap-3">
            <a href="/" data-svelte-reload >Home</a>
            <a href="/dashboard" data-svelte-reload>Dashboard</a>
            <a href="/listings/create" data-svelte-reload>Create Listing</a>
            <form method="POST" action="/signout" data-svelte-reload><button>Logout</button></form>
            <a href="/category/builds" data-svelte-reload>builds</a>     
            <a href="/dashboard/settings" data-svelte-reload>Settings</a>     
        </nav>
    </header>
{:else}
    <header class="container mx-auto p-4 mb-3 shadow">
        <nav>
            <a data-sveltekit-reload href="/">Home</a>
            <a href="/login">Login</a>
            <a href="/register">Register</a>
            <a href="/category/builds">builds</a>
        </nav>
    </header>
{/if}

<main class="container mx-auto px-4">
    <slot></slot>
</main>

<footer class="border-t container mx-auto pt-12 pb-32 px-4 lg:px-0">
    <div class="container">
    <div> 
      <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2100&q=80" class="h-12 w-12" alt="logo">
    </div>
    <div class="flex flex-wrap">
      <div class="w-full lg:w-2/5">
        <p class="text-gray-600 hidden lg:block mt-4 p-0 lg:pr-12">
          Boisterous he on understood attachment as entreaties ye devonshire. 
          In mile an form snug were been sell.
          Extremely ham any his departure for contained curiosity defective. 
          Way now instrument had eat diminution melancholy expression sentiments stimulated. 
        </p>
      </div>

      <div class="w-full mt-6 lg:mt-0 md:w-1/2 lg:w-1/5">
        <h6 class="font-semibold text-gray-700 mb-4">Company</h6>
        <ul>
          <li> <a href="/" class="block text-gray-600 py-2">Team</a> </li>
          <li> <a href="/" class="block text-gray-600 py-2">About us</a> </li>
          <li> <a href="/" class="block text-gray-600 py-2">Press</a> </li>
        </ul>
      </div>

      <div class="w-full mt-6 lg:mt-0 md:w-1/2 lg:w-1/5">
        <h6 class="font-semibold text-gray-700 mb-4">Content</h6>
        <ul>
          <li> <a href="/" class="block text-gray-600 py-2">Blog</a> </li>
          <li> <a href="/" class="block text-gray-600 py-2">Privacy Policy</a> </li>
          <li> <a href="/" class="block text-gray-600 py-2">Terms & Conditions</a> </li>
          <li> <a href="/" class="block text-gray-600 py-2">Documentation</a> </li>
        </ul>
      </div>

      <div class="w-full mt-6 lg:mt-0 md:w-1/2 lg:w-1/5">
        <h6 class="font-semibold text-gray-700 mb-4">Company</h6>
        <ul>
          <li> <a href="/" class="block text-gray-600 py-2">Team</a> </li>
          <li> <a href="/" class="block text-gray-600 py-2">About us</a> </li>
          <li> <a href="/" class="block text-gray-600 py-2">Press</a> </li>
        </ul>
      </div>

    </div>
</div>
  </footer>