class UserFetch {
    constructor (baseUrl, token) {
        this.baseUrl = baseUrl
        this.token = token
    }

    async get(path:string) {
        const response = await fetch(`${this.baseUrl}/${path}`, {
            method : "GET",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.token}`,
            }
        })
        return response
    }

    async post(path:string, body) {
        const response = await fetch(`${this.baseUrl}/${path}`, {
            method : "POST",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.token}`,
            },
            body: JSON.stringify(body)
        })
        return response
    }

    async postForm(path:string, formData) {
        const response = await fetch(`${this.baseUrl}/${path}`, {
            method : "POST",
            headers: {
                'Authorization': `Bearer ${this.token}`,
            },
            body: formData
        })
        return response
    }

    async delete(path:string) {
        const response = await fetch(`${this.baseUrl}/${path}`, {
            method : "DELETE",
            headers: {
                'Authorization': `Bearer ${this.token}`,
            }
        })
        return response
    }

    async put(path:string, formData) {
        const response = await fetch(`${this.baseUrl}/${path}`, {
            method : "PUT",
            headers: {
                'Authorization': `Bearer ${this.token}`,
            },
            body: formData
        })
        return response
    }

}

export default UserFetch