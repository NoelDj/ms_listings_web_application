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
      <img src="https://makersupplies.dk/img/cms/makersupplies-dk-logo-forum.png" class="h-12 w-12" alt="logo">
    </div>
    <div class="flex flex-wrap">
      <div class="w-full lg:w-2/5">
        <p class="text-gray-600 hidden lg:block mt-4 p-0 lg:pr-12">
          Join the makersupplies.dk forum and see other makers builds and or share your own. Discuss your ideas with maker friends and download resources
        </p>
      </div>

      <div class="w-full mt-6 lg:mt-0 md:w-1/2 lg:w-1/5">
        <h6 class="font-semibold text-gray-700 mb-4">makersupplies.dk</h6>
        <ul>
          <li> <a href="https://makersupplies.dk/" class="block text-gray-600 py-2">Shop</a> </li>
          <li> <a href="https://www.facebook.com/makersupplies.dk/" class="block text-gray-600 py-2">Facebook</a> </li>
          <li> <a href="https://www.youtube.com/@martinbarfoed5040" class="block text-gray-600 py-2">Youtube</a> </li>
        </ul>
      </div>

      <div class="w-full mt-6 lg:mt-0 md:w-1/2 lg:w-1/5">
        <h6 class="font-semibold text-gray-700 mb-4">Categories</h6>
        <ul>
          <li> <a href="http://converli.com/category/builds" class="block text-gray-600 py-2">Builds</a> </li>
          <li> <a href="http://converli.com/category/resources" class="block text-gray-600 py-2">Resources</a> </li>
          <li> <a href="http://converli.com/category/projects" class="block text-gray-600 py-2">Projects</a> </li>
          <li> <a href="http://converli.com/category/documents" class="block text-gray-600 py-2">Documents</a> </li>
        </ul>
      </div>

    </div>
</div>
  </footer>