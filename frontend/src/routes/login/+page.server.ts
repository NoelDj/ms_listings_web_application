import { redirect } from "@sveltejs/kit";
import { API_BASE_URL } from '$env/static/private';


export const actions = {
    default: async ({cookies, request}) => {
        const formData = await request.formData();

        const response = await fetch(`${API_BASE_URL}/auth/token`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            return;
        }

        const data = await response.json();

        console.log(data)

        const accessToken = data.access;
        const refreshToken = data.refresh;

        cookies.set("authToken", accessToken, {
            path: "/",
            secure: false,
        });

        cookies.set("refreshToken", refreshToken, {
            path: "/",
            secure: false,
        });


        console.log("Set cookies")
        console.log(cookies)

        redirect(301, "/dashboard")
    }
}
