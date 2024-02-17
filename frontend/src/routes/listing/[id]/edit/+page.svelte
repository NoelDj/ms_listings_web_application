<script>
  //import UserFetch from '../../utils/userFetch';
  import { onMount } from 'svelte';
  import { createEventDispatcher } from 'svelte';
  export let data;

  const {title,text,id} = data.listing
  const images = data.listing.images
  const files = data.listing.files
  console.log(images)

  //const { username, email } = data.decode;
  //const token = data.token;

  let content = text

  const dispatch = createEventDispatcher();
  let editor;

  export let toolbarOptions = [
    [{ header: 1 }, { header: 2 }, "blockquote", "link", "image", "video"],
    ["bold", "italic", "underline", "strike"],
    [{ list: "ordered" }, { list: "ordered" }],
    [{ align: [] }],
    ["clean"]
  ];

  onMount(async () => {
    const { default: Quill } = await import("quill");

    let quill = new Quill(editor, {
      modules: {
        toolbar: toolbarOptions
      },
      theme: "snow",
      placeholder: "Write your story...",
    });

    quill.root.innerHTML = content
    
    quill.on('text-change', () => {
      content = quill.root.innerHTML;
      dispatch('contentChange', content);
    });
  });
</script>

<style>
  @import 'https://cdn.quilljs.com/1.3.6/quill.snow.css';
</style>

<div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
  <h1>Update listing</h1>
  <a href="/listing/{id}">Preview</a>
  <div class="mb-4">
      <form action="?/updateListing" method="POST" enctype="multipart/form-data">
          <input type="hidden" name="text" value={content} id="">
          <label class="block text-grey-darker text-sm font-bold mb-2" for="title">Title</label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" id="title" type="text" name="title" value="{title}">
          <div class="markdown mt-2 mb-4">
              <div class="editor-wrapper">
                  <div class="h-40" bind:this={editor} />
              </div>
          </div>
          <div>
              <label for="Images">Images</label>
              <input type="file" name="images" id="" multiple>
          </div>
          <div>
            <br>
            {#if images.length > 0}
            <fieldset>
              <legend>Remove images:</legend>
              {#each images as image, index (index)}
                {#if index !== 0}
                  <div>
                    <label for="scales">{image.src}</label>
                    <input type="checkbox" id="scales" name="remove_images" value="{image.id}"/>
                  </div>
                {/if}
              {/each}
              
            </fieldset>
            {/if}
          </div>
         
          <br>
          <div>
              <label for="files">Files</label>
              <input type="file" name="files" id="" multiple>
          </div>
          <div>
            <br>
            {#if files.length > 0}
            <fieldset>
              <legend>Remove files:</legend>
              {#each files as file}
              <div>
                <label for="scales">{file.file}</label>
                <input type="checkbox" id="scales" name="remove_files" value="{file.id}"/>
              </div>
              {/each}
              
            </fieldset>
            {/if}
          </div>
          <button class="bg-sky-600 hover:bg-blue-dark mt-5 text-white font-bold py-2 px-4 rounded" type="submit">Update</button>
      </form>
  </div>
</div>