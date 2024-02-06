import { API_BASE_URL, BASE_URL } from "$env/static/private"
import { getUser } from "../../../utils/auth"
import UserFetch from "../../../utils/userFetch"

export const load = async ({cookies}) => {
    const user = getUser(cookies.get('authToken'))

    const response = await fetch(`${API_BASE_URL}/users/${user.username}`)
    const data = await response.json()
    return {user: data.user, baseUrl: BASE_URL}
}

export const actions = {
    updateUser: async ({cookies, request, params}) => {
        
        const token = cookies.get('authToken')
        const user = getUser(token)
        const formData = await request.formData()

        const path = "users/" + user.username
        const useFetch = new UserFetch('http://localhost:8000/api', token)
        const response = await useFetch.put(path, formData)
        const data = await response.json()
        
    } 
}