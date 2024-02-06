// token.js
import { writable } from 'svelte/store';

let initialToken = '';

// Check if the code is running in the browser context
if (typeof window !== 'undefined') {
    initialToken = localStorage.getItem('token') || '';
}

export const token = writable(initialToken);

// Update token function
export function updateToken(newToken) {
    token.set(newToken);
    
    if (typeof window !== 'undefined') {
        localStorage.setItem('token', newToken);
    }
}
