import { API_BASE_URL } from "$env/static/private";
import UserFetch from "../../../utils/userFetch"
import { error, redirect } from "@sveltejs/kit";
import { fail } from '@sveltejs/kit';

export const actions = {
    default: async ({cookies, request}) => {
        const formData = await request.formData()
        const files = formData.getAll('files')
        files[0].size === 0 || files[0].name === '' && formData.delete('files')
        const images = formData.getAll('images')
        

        if (images[0].size === 0 || images[0].name === '') {
            fail(400, { images, incorrect: true })
        } else {
            const token = await cookies.get("authToken")
            const useFetch = new UserFetch(API_BASE_URL, token)
            const response = await useFetch.postForm('listings', formData)
            const data = await response.json()
            console.log(data)
            const { id } = data
            if (response.ok) {
                redirect(301, `/listing/${id}`)
            }
        }
    }
}