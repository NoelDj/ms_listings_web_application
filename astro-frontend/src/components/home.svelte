<script>
    /* import { token } from '../stores/token';
    let responseMessage = '';

    async function accessProtectedEndpoint() {
        const storedToken = $token; // Access the token value from the store
        console.log(storedToken)
        if (!storedToken) {
            // Redirect or handle unauthorized access
            return;
        }

        const response = await fetch('http://localhost:8000/api/dashboard/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${storedToken}`
            }
        });

        
        if (response.ok) {
            const message = await response.json();
            console.log(message)
        } else {
            page.redirect(1)
        }
        console.log(response)
    }

    accessProtectedEndpoint(); */

    
</script>

<div class="flex justify-between container mx-auto p-4">
    <h1>Hello, you are logged in</h1>
</div>