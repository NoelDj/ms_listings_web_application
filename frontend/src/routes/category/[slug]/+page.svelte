<script>
    import ListingsGrid from '../../../components/ListingsGrid.svelte';
    export let data
    const {name, description} = data.category
    const informationSet = data.listings
    const baseImagePath = data.baseUrl
</script>
<h1>{name}</h1>
<p>{description}</p>

<ListingsGrid {informationSet} {baseImagePath}></ListingsGrid>