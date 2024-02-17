import { API_BASE_URL } from "$env/static/private";
import UserFetch from "../../utils/userFetch"
import { jwtDecode } from "jwt-decode"

export const load = async ({locals}) => {
    const token = locals.token;
    const decode = jwtDecode(token)
    console.log(decode.user_id)
    const userId = decode.user_id.toString()
    
    const useFetch = new UserFetch(API_BASE_URL, token)
    const response = await useFetch.get(`listings?owner_id=${userId}`)
    const data = await response.json()
    const informationSet = data
    return { informationSet }
}

export const actions = {
    deleteListing: async ({locals, request}) => {
        const formData = await request.formData();
        const id = formData.get('id');
        const token = locals.token;

        const useFetch = new UserFetch(API_BASE_URL, token)
        const path = "listings/" + id
        await useFetch.delete(path)

    }
};