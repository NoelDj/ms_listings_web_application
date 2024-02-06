import { isValid, refreshAuthToken, setCookies, isExpiring, isExpired } from "./utils/auth"
import { API_BASE_URL } from "$env/static/private";
import { redirect } from "@sveltejs/kit";

export async function handle({ event, resolve }) {
	const token = await event.cookies.get('authToken')
	event.locals.token = token
    const pathName = event.url.pathname
    let isAuthenticated = isValid(token)
    const protectedRoutes = ['/dashboard', '/dashboard/settings', '/listings/create', 'listings/3/edit']
    const authRoutes = ['/login', '/register']
    
    
    if (authRoutes.includes(pathName) && isAuthenticated) redirect(301, '/dashboard')

    if (!protectedRoutes.includes(pathName)) {
        const response = await resolve(event);
        return response;
    }

    if (token && isExpired(token)) {
        const refreshToken = event.cookies.get('refreshToken')
        const response = await refreshAuthToken(refreshToken, API_BASE_URL)
        const data = await response.json()
        isAuthenticated = isValid(data.access)
        setCookies(event, data)
    }
 
    if (!isAuthenticated) redirect(301, '/login')
    
    
    

	const response = await resolve(event);
    return response;
}


