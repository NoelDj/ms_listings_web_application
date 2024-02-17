<script>
    import { enhance } from '$app/forms';


    export let form
</script>
<form method="POST" action="?/login">
    
    {#if form?.succes}
        <p>Success</p>
    {/if}
    {#if form?.email?.missing}<p class="error">The email field is required</p>{/if}
    {#if form?.password?.incorrect}<p class="error">Invalid credentials!</p>{/if}

	<label>
		Email
		<input name="email" type="text" value="{form?.email?.value || ''}">
	</label>
	<label>
		Password
		<input name="password" type="password">
	</label>
	<button>Log in</button>
</form>