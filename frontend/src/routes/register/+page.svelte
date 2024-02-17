<script>
    export let form
</script>

<div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
    <h1>Register</h1>

    <div class="mb-4">
    <form method="POST">
        <label class="block text-grey-darker text-sm font-bold mb-2" for="email">Username</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" id="username" type="text" name="username" value="{form?.username?.value || ''}">
        {#if form?.username?.missing }<p class="error">Please enter an username</p>{/if}
        {#if form?.username?.exists }<p class="error">Username already exists</p>{/if}
        <label class="block text-grey-darker text-sm font-bold mb-2" for="email">Email</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" id="email" type="text" name="email"value="{form?.email?.value || ''}">
        {#if form?.email?.missing }<p class="error">Please enter an email</p>{/if}
        {#if form?.email?.exists }<p class="error">Email already exists</p>{/if}
        <label class="block text-grey-darker text-sm font-bold mb-2" for="password">Password</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 mb-2 text-grey-darker" name="password" type="password" value="{form?.password?.value || ''}">
        {#if form?.password?.missing }<p class="error">Please enter a password</p>{/if}
        <label class="block text-grey-darker text-sm font-bold mb-2" for="password2">Confirm</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 mb-2 text-grey-darker" name="password2" type="password" value="{form?.password2?.value || ''}">
        {#if form?.password?.passwordErrors }
            {#each form.password.passwordErrors as error}
            <p class="error">{error}</p>
            {/each}
        {/if}
        <div class="flex items-center justify-between">
        <button class="bg-sky-600 hover:bg-blue-dark text-white font-bold py-2 px-4 rounded" type="submit">
            Sign In
        </button>
        <!-- <a class="inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker" href="/">
            Forgot Password?
        </a> -->
        </div>
    </form>
    </div>
</div>
    