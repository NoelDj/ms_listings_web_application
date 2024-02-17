<script>
    import ListingsGrid from '../../../components/ListingsGrid.svelte';
    export let data

    const {bio, username} = data.user
    const informationSet = data.listings
    const baseImagePath = data.baseUrl
    
</script>



<h1>{username}</h1>
{#if bio}<p>{bio}</p>{/if}

<ListingsGrid {informationSet} {baseImagePath}></ListingsGrid>