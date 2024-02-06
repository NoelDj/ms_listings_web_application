import { redirect } from "@sveltejs/kit";
import { API_BASE_URL } from '$env/static/private';


export const actions = {
    default: async (e) => {
        const formData = await e.request.formData();
        
        const response = await fetch(`${API_BASE_URL}/auth/token`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            return;
        }

        const data = await response.json();

        const accesToken = data.access;
        const refreshToken = data.refresh;


        e.cookies.set("authToken", accesToken, {
            path: "/",
        });

        e.cookies.set("refreshToken", refreshToken, {
            path: "/",
        });

        redirect(301, "/dashboard")
    }
}
