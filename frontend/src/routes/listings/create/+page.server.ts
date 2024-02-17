import { API_BASE_URL } from "$env/static/private";
import UserFetch from "../../../utils/userFetch"
import { redirect } from "@sveltejs/kit";
import { fail } from '@sveltejs/kit';

interface DataObject {
    [key: string]: { value?: string; missing?: boolean; incorrect?: boolean; exists?: boolean; errors?: Array<string>}
}

export const actions = {
    default: async ({cookies, request}) => {
        const formData = await request.formData()
        const files = formData.getAll('files')
        const images = formData.getAll('images')
        //remove the file with empty content from the form data
        files.length > 0 && (files[0].size === 0 || files[0].name === '') && formData.delete('files')
        images.length > 0 && (images[0].size === 0 || images[0].name === '') && formData.delete('images')

        const token = await cookies.get("authToken")
        const useFetch = new UserFetch(API_BASE_URL, token)
        const response = await useFetch.postForm('listings', formData)
        const data = await response.json()
        const { id } = data
        if (response.ok) {
            redirect(301, `/listing/${id}`)
        } else {
            
            const titleValue = formData.get('title')
            const textValue = formData.get('text')
            console.log(data)

            const dataObject: DataObject = {
                images : {},
                title : {value: titleValue || ''},
                text : {value: textValue || ''}
            }

            if (data.error === 'No file uploaded') {
                dataObject.images.missing = true
                return fail(400, dataObject)
            }

            for (const property in dataObject) {
                if (property === 'images' || property === 'files') {
                    continue
                }
                if (data.message[property] && data.message[property][0] === 'This field may not be blank.') {
                    dataObject[property].missing = true
                }
            }

            if (Object.values(dataObject).some(field => field.missing || field.incorrect || field.exists || field.errors)) {
                return fail(400, dataObject)
            }

        }
    }
}