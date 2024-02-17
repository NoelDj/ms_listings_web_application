<script lang="ts">
    //import UserFetch from '../../utils/userFetch';
    import { onMount } from 'svelte'
    import { createEventDispatcher } from 'svelte'
    export let form
  
    let content = form?.title?.value || ''
  
    const dispatch = createEventDispatcher()
    let editor
  
    export let toolbarOptions = [
      [{ header: 1 }, { header: 2 }, "blockquote", "link"],
      ["bold", "italic", "underline", "strike"],
      [{ list: "bullet" }, { list: "ordered" }],
      [{ align: [] }],
      ["clean"]
    ]
  
    onMount(async () => {
      const { default: Quill } = await import("quill")
  
      let quill = new Quill(editor, {
        modules: {
          toolbar: toolbarOptions
        },
        theme: "snow",
        placeholder: "Write your story...",
      });
      
      quill.on('text-change', () => {
        content = quill.root.innerHTML;
        dispatch('contentChange', content);
      })
    })
</script>

<style>
    @import 'https://cdn.quilljs.com/1.3.6/quill.snow.css';
</style>

<div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col">
    <h1>Post article</h1>
    <div class="mb-4">
        <form method="POST" enctype="multipart/form-data">
            <input type="hidden" name="text" value={content} id="">
            <label class="block text-grey-darker text-sm font-bold mb-2" for="title">Title</label>
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker" id="title" type="text" name="title" value="{form?.title?.value || ''}">
            {#if form?.title?.missing }<p class="error">Please enter a title</p>{/if}
            <label for="countries" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select an option</label>
            <select name="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
                <option selected value="1">Builds</option>
                <option value="2">Resources</option>
                <option value="3">Projects</option>
                <option value="4">Documents</option>
            </select>
            <div class="markdown mt-2 mb-4">
                <div class="editor-wrapper">
                    <div class="h-40" bind:this={editor} />
                </div>
            </div>
            {#if form?.text?.missing }<p class="error">Please enter text</p>{/if}
            <p></p>
            <div>
                <label for="Images">Images</label>
                <input type="file" name="images" id="" multiple>
            </div>
            {#if form?.images?.missing }<p class="error">Please upload an image</p>{/if}
            <div>
                <label for="files">Files</label>
                <input type="file" name="files" id="" multiple>
            </div>
            <button class="bg-sky-600 hover:bg-blue-dark mt-5 text-white font-bold py-2 px-4 rounded" type="submit">Create</button>
        </form>
    </div>
</div>