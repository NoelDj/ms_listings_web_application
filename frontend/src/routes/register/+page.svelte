<script>
    export let data
</script>

<!-- {#if registrated}
    <p>Registration successfull, login beneath</p>
    <a href="/login">Login</a>
{/if} -->
    
<div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
    <h1>Register</h1>

    <div class="mb-4">
    <form method="POST">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="email">Username</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" id="username" type="text" name="username" value="assa">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="email">Email</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" id="email" type="text" name="email" value="noedl.klp@gmail.com">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="password">Password</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 mb-2 text-grey-darker" name="password" type="password" value="deXSA1234">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="password2">Confirm</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 mb-2 text-grey-darker" name="password2" type="password" value="deXSA1234">
        <div class="flex items-center justify-between">
        <button class="bg-sky-600 hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="submit">
            Sign In
        </button>
        <a class="inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker" href="/">
            Forgot Password?
        </a>
        </div>
    </form>
    </div>
</div>
    