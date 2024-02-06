import { jwtDecode } from "jwt-decode";
import dayjs from "dayjs";

export async function fetchAuthToken(credentials) {
    const response = await fetch(`${API_BASE_URL}/auth/token`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
    });

    if (!response.ok) {
        throw new Error('Failed to fetch auth token');
    }

    return await response.json();
}

export const isValid = (token) => {
    if (!token || token === undefined) return false
    const decode = jwtDecode(token)
    const isExpired = dayjs.unix(decode.exp).diff(dayjs()) > 1
    return isExpired
}

export const isExpired = (token: string): Boolean => {
    const decode = jwtDecode(token)
    const isExpired = dayjs.unix(decode.exp).diff(dayjs()) <= 0
    return isExpired
}

export const isExpiring = (token) => {
    const decode = jwtDecode(token)
    dayjs.unix(decode.exp).diff(dayjs()) > 120
}

export async function refreshAuthToken(refreshToken, baseUrl) {
    const formData = new FormData()
    formData.append('refresh', refreshToken)
    const response = await fetch(`${baseUrl}/auth/token/refresh`, {
        method: 'POST',
        body: formData,
    });
    return response
}

export const setCookies = (event, tokens) => {
    event.locals.token = tokens.access
    event.cookies.set("authToken", tokens.access, {
        path: "/",
    });
    
    event.cookies.set("refreshToken", tokens.refresh, {
        path: "/",
    });
}

export const getUser = (token) => {
    const decode = jwtDecode(token)
    return decode
}