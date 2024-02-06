<script>
    import authStore from '../stores/auth';

    const {loginUser} = authStore

    let email = '';
    let password = '';

    const handleLogin = () => {
      loginUser(email,password)
    }
    
</script>

<!-- Login form -->

<div class="container flex justify-center m-5">
    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-64" on:submit|preventDefault="{handleLogin}">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
            Username or Email
          </label>
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="email" type="text" bind:value="{email}" placeholder="Email"  />
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input
            class="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            id="password"type="password" bind:value="{password}" placeholder="Password" />
        </div>
        <div class="flex items-center justify-between">
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
            Sign In
          </button>
        </div>
      </form>
</div>
    