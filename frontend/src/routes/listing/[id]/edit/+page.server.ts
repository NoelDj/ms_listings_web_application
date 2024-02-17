import { API_BASE_URL } from "$env/static/private"
import UserFetch from "../../../../utils/userFetch"

export async function load({ params }) {
    const response = await fetch(API_BASE_URL + "/listings/" + params.id)
    const data = await response.json()

    return {"listing":data.listing}
}

export const actions = {
    updateListing: async ({cookies, request, params}) => {
        const token = cookies.get('authToken')
        const formData = await request.formData()

        console.log(formData.get('remove_images'))

        const uploads = ['files', 'images'];

        const removeEmptyUploads = (list) => {
            list.forEach(e => {
                const uploads = Array.from(formData.getAll(e))
                if (uploads[0].size === 0 || uploads[0].name == '') {
                    formData.delete(e)
                }   
            })
        }

        removeEmptyUploads(uploads)

        const path = "listings/" + params.id
        const useFetch = new UserFetch(API_BASE_URL, token)
        const response = await useFetch.put(path, formData)
        const data = await response.json()

        console.log(data)
        
    } 
}