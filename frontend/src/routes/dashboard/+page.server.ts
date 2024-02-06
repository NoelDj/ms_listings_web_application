import UserFetch from "../../utils/userFetch"
import { jwtDecode } from "jwt-decode"

export const load = async ({locals}) => {
    const token = locals.token;
    const decode = jwtDecode(token)
    console.log(decode.user_id)
    const userId = decode.user_id.toString()

    const useFetch = new UserFetch('http://localhost:8000/api', token)
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

        const useFetch = new UserFetch('http://localhost:8000/api', token)
        const path = "listings/" + id
        const response = await useFetch.delete(path)

        return true;
    }
};