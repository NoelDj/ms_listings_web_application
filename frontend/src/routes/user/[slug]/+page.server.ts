import { API_BASE_URL, BASE_URL } from '$env/static/private';
import { error } from "@sveltejs/kit";

export async function load({ params }) {
    const response = await fetch(`${API_BASE_URL}/users/${params.slug}`)
    const data = await response.json()
    
    if (!response.ok) {
        error(404, {
          message: 'Not found'
        })
    }
    
    const user = data.user
    const responseListings = await fetch(`${API_BASE_URL}/listings?owner_id=${user.id}`)
    const dataListings = await responseListings.json()
    const listings = dataListings
    const baseUrl = BASE_URL
    
    return {
        user,
        listings,
        baseUrl
    }
}