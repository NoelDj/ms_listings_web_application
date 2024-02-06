<script>
    import authStore from "../stores/auth"

    const {logoutUser, auth} = authStore

    const handleClick = () => {
        logoutUser
        alert("Logged Out")
    }
</script>


<!-- Text Header -->
<header class="w-full container mx-auto">
    <div class="flex flex-col items-center py-12">
        <a class="font-bold text-gray-800 uppercase hover:text-gray-700 text-5xl" href="/">
            Ms Listings
        </a>
        <p class="text-lg text-gray-600">
            Listing and Resources For Makers
        </p>
    </div>
</header>

<!-- Topic Nav -->
<nav class="w-full py-4 border-t border-b bg-gray-100">
    <div class="block sm:hidden">
        <a
            href="#"
            class="block md:hidden text-base font-bold uppercase text-center flex justify-center items-center"
        >
            Topics <i class="fas ml-2"></i>
        </a>
    </div>
    <div :class="open ? 'block': 'hidden'" class="w-full flex-grow sm:flex sm:items-center sm:w-auto">
        <div class="w-full container mx-auto flex flex-col sm:flex-row items-center justify-center text-sm font-bold uppercase mt-0 px-6 py-2">
            <a href="/register" class="hover:bg-gray-400 rounded py-2 px-4 mx-2">Register</a>
            <a href="/login" class="hover:bg-gray-400 rounded py-2 px-4 mx-2">Login</a>
            <a href="/home" class="hover:bg-gray-400 rounded py-2 px-4 mx-2">Home</a>
            <button class="hover:bg-gray-400 rounded py-2 px-4 mx-2" on:click="{handleClick}">LOG OUT</button>
        </div>
    </div>
</nav>