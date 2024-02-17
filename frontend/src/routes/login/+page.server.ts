import { redirect } from "@sveltejs/kit"
import { API_BASE_URL } from '$env/static/private'
import { fail } from '@sveltejs/kit';

interface DataObject {
    [key: string]: { value?: string; missing?: boolean; incorrect?: boolean }
}


export const actions = {
    default: async ({cookies, request}) => {
        const formData = await request.formData()
        const emailValue:string = formData.get('email')

        const response = await fetch(`${API_BASE_URL}/auth/token`, {
            method: 'POST',
            body: formData
        })

        const data = await response.json()
        
        const dataObject: DataObject = {
            email: { value: emailValue || '' },
            password: {}
        }
        
        if (!response.ok) {
            if (data.email) {
                dataObject.email.missing = true
            }

            if (data.password) {
                dataObject.password.missing = true
            }

            if (data.detail) {
                dataObject.password.incorrect = true
            }
    
            if (Object.values(dataObject).some(field => field.missing || field.incorrect)) {
                return fail(400, dataObject);
            }
        }

        const accessToken = data.access
        const refreshToken = data.refresh

        cookies.set("authToken", accessToken, {
            path: "/",
            secure: false,
        })

        cookies.set("refreshToken", refreshToken, {
            path: "/",
            secure: false,
        })

        redirect(301, "/dashboard")
    }
}
