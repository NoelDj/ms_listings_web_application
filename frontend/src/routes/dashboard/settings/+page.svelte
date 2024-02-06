<script>
    export let data
    const {bio, username, image} = data.user
    const {baseUrl} = data
</script>

<div class="max-w-5xl mx-auto my-8 p-6 bg-white rounded-md shadow-md">
    <h2 class="text-2xl font-semibold mb-6">User Settings</h2>
    <p>{username}</p>
    <form method="POST" action="?/updateUser" enctype="multipart/form-data">
    <div class="grid grid-cols-2 gap-6">
      <!-- Left Column - Bio Section -->
      <div>
        <label for="bio" class="block text-gray-600 text-sm font-semibold mb-2">Bio</label>
        <textarea id="bio" name="bio" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500" rows="4" placeholder="Enter your bio">{bio}</textarea>
      </div>
  
      <!-- Right Column - Email Section -->
      <div>
        <div>
            <img src="{`${baseUrl}${image}`}" alt="">
        </div>
        <label for="image" class="block text-gray-600 text-sm font-semibold mb-2">Image</label>
        <input type="file" id="image" name="image" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500">
      </div>
    </div>
    
    <button class="mt-6 bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:shadow-outline-blue">Save Changes</button>
    </form>
  </div>
  
  