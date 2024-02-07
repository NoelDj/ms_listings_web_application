<script>

    import {onMount} from 'svelte'

    export let data
    const {isAuthenticated} = data
    const userId = data.userId
    const {isLiked} = data
    const {likeId} = data
    const {title, text, created_at, id, like_count} = data.listing
    const {username, email, bio, image} = data.listing.owner
    const {name} = data.listing.category
    const files = data.listing.files
    const listingImage = data.listing.images[0].src || ""
    const baseImagePath = data.baseImagePath
 
    const comments = data.comments
    
    const imagePath = baseImagePath + listingImage
    
    const images = data.listing.images

</script>



    <div class="my-16">

      <div class="mb-4 md:mb-0 w-full mx-auto relative">
        <div class="px-4 lg:px-0">
          <h2 class="text-4xl font-semibold text-gray-800 leading-tight">
            {title}
          </h2>
          <div class="flex gap-3 my-3">
            <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Likes: {like_count}</span>
            <span class="inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">{created_at}</span>
            <span class="inline-flex items-center rounded-md bg-indigo-50 px-2 py-1 text-xs font-medium text-indigo-700 ring-1 ring-inset ring-indigo-700/10"><a href="/category/{name}">{name}</a></span>
            {#if isAuthenticated}
              {#if isLiked}
              <form method="POST" action="?/deleteLike">
                <input type="hidden" name="like_id" value="{likeId}">
                <button class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
                  Remove Like
                </button>
              </form>
              {:else}
              <form method="POST" action="?/likeListing">
                <input type="hidden" name="listing_id" value="{id}">
                <button class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
                  Like
                </button>
              </form>
              {/if}
            {/if}
          </div>
        </div>
        <img src="{imagePath}" class="w-full object-cover lg:rounded" style="height: 28em;"/>
      </div>
      

      <div class="flex flex-col lg:flex-row lg:space-x-12">

        <article class="article px-4 lg:px-0 mt-12 text-gray-700 text-lg leading-relaxed w-full lg:w-3/4">
          {@html `${text}`}
        </article>


        <div class="w-full lg:w-1/4 m-auto mt-12 max-w-screen-sm">
          <div class="p-4 border-t border-b md:border md:rounded">
            <div class="flex py-2">
              <img src="{baseImagePath + image}"
                class="h-10 w-10 rounded-full mr-2 object-cover" />
              <div>
                <p class="font-semibold text-gray-700 text-sm"> <a href="/user/{username}">{username}</a></p>
                <p class="font-semibold text-gray-600 text-xs"> <a href="mailto:{email}">{email}</a></p>
              </div>
            </div>
            <p class="text-gray-700 py-3">{bio}</p>
            <button class="px-2 py-1 text-gray-100 bg-green-700 flex w-full items-center justify-center rounded">
              Follow 
              <i class='bx bx-user-plus ml-2' ></i>
            </button>
          </div>
          <div>
            <ul>
            {#each files as {file}}
              <li><a href="{baseImagePath}{file}" download="{file}">{file}</a></li>
            {/each}
            </ul>
          </div>
        </div>

      </div>
      <div class="flex gap-2 mt-2">
        {#each images as image, index (index)}
          {#if index !== 0}
            <div><img src="{baseImagePath + image.src}" style="height: 200px;"></div>
          {/if}
        {/each}
      </div>
      {#if isAuthenticated}
      <div>
        <form class="mt-6" method="POST" action="?/postComment">
          <div class="py-2 px-4 mb-4 bg-white rounded-lg rounded-t-lg border border-gray-200">
              <label for="comment" class="sr-only">Your comment</label>
              <textarea id="comment" rows="6"
                  class="px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none"
                  placeholder="Write a comment..." name="text" required></textarea>
          </div>
          <input type="hidden" value="{id}" name="listing">
          <button type="submit"
              class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-primary-200">
              Post comment
          </button>
        </form>
      </div>
      {/if}
      <div class="mt-10">
      {#each comments as comment}
        <div class="relative grid grid-cols-1 gap-4 p-4 mb-8 border rounded-lg bg-white shadow-lg">
          <div class="relative flex gap-4">
              <img src="{baseImagePath + comment.user.image}" class="relative rounded-lg -top-8 -mb-4 bg-white border h-20 w-20" alt="" loading="lazy">
              <div class="flex flex-col w-full">
                  <div class="flex flex-row justify-between">
                      <p class="relative text-xl whitespace-nowrap truncate overflow-hidden"><a href="/user/{comment.user.username}">{comment.user.username}</a></p>
                      <a class="text-gray-500 text-xl" href="#"><i class="fa-solid fa-trash"></i></a>
                  </div>
                  <div class="flex gap-3 align-center">
                    <p class="text-gray-400 text-sm">{comment.created_at}</p>
                    {#if comment.user.id == userId && isAuthenticated}
                    <form method="POST" action="?/deleteComment">
                      <input type="hidden" name="comment_id" value="{comment.id}">
                      <button>Delete</button>
                    </form>
                    {/if}
                  </div>
              </div>
          </div>
          <p class="-mt-4 text-gray-500">{comment.text}</p>
      </div>
      {/each}
    </div>
    </div>