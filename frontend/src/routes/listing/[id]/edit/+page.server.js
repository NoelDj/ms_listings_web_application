import UserFetch from "../../../../utils/userFetch"

export async function load({ params }) {

    const response = await fetch("http://localhost:8000/api/listings/" + params.id)
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
        const useFetch = new UserFetch('http://localhost:8000/api', token)
        const response = await useFetch.put(path, formData)
        
    } 
}