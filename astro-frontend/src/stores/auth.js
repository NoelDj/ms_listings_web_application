import {
    writable
} from "svelte/store";
import { onMount } from 'svelte';
import jwt_decode from "jwt-decode";



const storedAuthTokens = typeof localStorage !== 'undefined' ? localStorage.getItem('authTokens') : null;
let authTokens = writable(storedAuthTokens ? JSON.parse(storedAuthTokens) : null);
let user = writable(storedAuthTokens ? jwt_decode(JSON.parse(storedAuthTokens).access) : null);

const loginUser = async function (email, password) {
    console.log(email,password)
    const response = await fetch("http://localhost:8000/api/token/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            email,
            password,
        }),
    });

    const data = await response.json();
    
    if (response.status === 200) {
        console.log(data)
        /* 
        user.set(jwt_decode(data.access)); */
        authTokens.set(data);
        localStorage.setItem("authTokens", JSON.stringify(data));
        alert("logged in")
    } else {
        alert("not logged in")
    }
    
};

const registerUser = async function (email, username, password, password2) {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email,
                username,
                password,
                password2,
            }),
        });

        if (response.status === 201) {
            alert("logged in")
        } else {
            alert("Not logged in")
        }
    } catch (error) {
        console.error("Registration error:", error);
    }
};

const logoutUser = function () {
    authTokens.set(null);
    user.set(null);
    localStorage.removeItem("authTokens");
};

const authStore = {
    /* 
    user,
    loading,
    registerUser,*/
    authTokens,
    logoutUser, 
    loginUser,
};

export default authStore