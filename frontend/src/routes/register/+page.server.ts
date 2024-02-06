import { redirect } from '@sveltejs/kit';
import { jwtDecode } from 'jwt-decode';
import dayjs from "dayjs"
import { API_BASE_URL } from '$env/static/private';

export const load = async (e) => {
    const token = e.cookies.get("authToken")
    if(token){
        const decode = jwtDecode(token)
        const isExpired = dayjs.unix(decode.exp).diff(dayjs()) < 1
        if (!isExpired) redirect(301, "/dashboard")
    }
}

export const actions = {
    default: async ({request}) => {
        const requestData = await request.formData()
        const formData = Object.fromEntries(requestData)
        const response = await fetch(`${API_BASE_URL}/users`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        //const data = await response.json()
        if (response.ok) {
            redirect(301, '/login')
        }
    }
}
