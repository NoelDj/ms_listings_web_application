import { API_BASE_URL, BASE_URL } from '$env/static/private';

/** @type {import('./$types').PageLoad} */
export async function load({ url }) {
    let endpoint = `${API_BASE_URL}/listings`
    const filterParams = [];

    url.searchParams.forEach((value, key) => {
        filterParams.push({ 'key': key, 'value': value });
    });

    for (let i = 0; i < filterParams.length; i++) {
        const prefix = i == 0 ? '?' : '&'
        endpoint += `${prefix}${filterParams[i].key}=${filterParams[i].value}`
    }


    const baseUrl = BASE_URL
    const response = await fetch(endpoint)
    const data = await response.json()
    const listings = data
    return {
        listings,
        baseUrl
    }
}

