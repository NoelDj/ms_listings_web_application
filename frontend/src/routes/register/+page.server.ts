import { redirect } from '@sveltejs/kit';
import { jwtDecode } from 'jwt-decode';
import dayjs from "dayjs"
import { API_BASE_URL } from '$env/static/private';
import { fail } from '@sveltejs/kit';

export const load = async (e) => {
    const token = e.cookies.get("authToken")
    if(token){
        const decode = jwtDecode(token)
        const isExpired = dayjs.unix(decode.exp).diff(dayjs()) < 1
        if (!isExpired) redirect(301, "/dashboard")
    }
}

interface DataObject {
    [key: string]: { value?: string; missing?: boolean; incorrect?: boolean; exists?: boolean; passwordErrors?: Array<string>}
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
        const data = await response.json()
        const userNameValue = requestData.get('username')
        const emailValue = requestData.get('email')
        
        
        if (response.ok) {
            redirect(301, '/login')
        } else {

            const dataObject: DataObject = {
                username: { value: userNameValue || '' },
                email: { value: emailValue || '' },
                password: {},
                password2: {}
            }

            for (const property in dataObject) {
                if (data.message[property] && data.message[property][0] === 'This field may not be blank.') {
                    dataObject[property].missing = true
                }
            }

            if (data.message.email && data.message.email[0] === 'user with this email already exists.') {
                dataObject.email.exists = true
            }

            if (data.message.username && data.message.username[0] === 'A user with this username already exists.') {
                dataObject.username.exists = true
            }

            if (data.message.password) {
                dataObject.password.passwordErrors = data.message.password
            }
    
            if (Object.values(dataObject).some(field => field.missing || field.incorrect || field.exists || field.passwordErrors)) {
                return fail(400, dataObject);
            }
            
        }
    }
}
