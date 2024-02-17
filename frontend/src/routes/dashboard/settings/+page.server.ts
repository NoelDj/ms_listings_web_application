import { API_BASE_URL, BASE_URL } from "$env/static/private"
import { getUser } from "../../../utils/auth"
import UserFetch from "../../../utils/userFetch"

interface UserData {
    username: string;
}

interface LoadFunctionResponse {
    user: UserData;
    baseUrl: string;
}

export const load = async ({cookies}) => {
    const user = getUser(cookies.get('authToken'))

    const response = await fetch(`${API_BASE_URL}/users/${user.username}`)
    const data = await response.json()
    return {user: data.user, baseUrl: BASE_URL}
}

export const actions = {
    updateUser: async ({cookies, request}) => {
        
        const token = cookies.get('authToken')
        const user = getUser(token)
        const formData = await request.formData()

        const path = "users/" + user.username
        const useFetch = new UserFetch(API_BASE_URL, token)
        await useFetch.put(path, formData)
        
    } 
}