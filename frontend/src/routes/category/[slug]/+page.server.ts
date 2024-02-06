import { error, redirect } from '@sveltejs/kit';
import { API_BASE_URL, BASE_URL } from '$env/static/private';

export async function load({ params, url }) {

    const responseCategory = await fetch(`${API_BASE_URL}/categories/${params.slug}`)
    const dataCategory = await responseCategory.json()
    
    if (!responseCategory.ok) {
        error(404, {
          message: 'Not found'
        });
    }

    const categoryId = dataCategory.category.id

    let endpoint = `${API_BASE_URL}/listings?category_id=${categoryId}`
    
    const filterParams = [];

    url.searchParams.forEach((value, key) => {
        key !== 'category_id' && filterParams.push({ 'key': key, 'value': value });
    })

    for (let i = 0; i < filterParams.length; i++) {
      endpoint += `&${filterParams[i].key}=${filterParams[i].value}`
    }
    
    const responseListings = await fetch(endpoint)
    const dataListings = await responseListings.json()

    if (!responseListings.ok) {
      error(404, {
        message: 'Not found'
      });
    }
    
    const category = dataCategory.category
    const baseUrl = BASE_URL

    let listings = dataListings
    return {
        category,
        listings,
        baseUrl       
    }
  }