<script>



    let result;
    let errors = {
            email : "",
            username : "",
            password : "",
            password2 : ""
        }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = Object.fromEntries(new FormData(e.target))
        try {
            const response = await fetch('http://localhost:8000/api/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();
            
            if (result.email) errors.email = result.email.join("<br>")
            if (result.username) errors.username = result.username.join("<br>")
            if (result.password) errors.password = result.password.join("<br>")
            if (result.password2) errors.password2 = result.password2.join("<br>")
            console.log(result)
            console.log(errors)
        } catch (error) {
            console.error('Error:', error);
        }
    };

</script>

<section class="vh-100">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col col-xl-10">
                <div class="card" style={{ borderRadius: "1rem" }}>
                    <div class="row g-0">
                        <div class="col-md-6 col-lg-5 d-none d-md-block">
                            <img
                                src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp"
                                alt="login form"
                                class="img-fluid"
                                style="border-radius: 1rem 0 0 1rem;"
                            />
                        </div>
                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                            <div class="card-body p-4 p-lg-5 text-black">
                                <form on:submit={handleSubmit}>
                                    <div class="d-flex align-items-center mb-3 pb-1">
                                        <i
                                            class="fas fa-cubes fa-2x me-3"
                                            style={{ color: "#ff6219" }}
                                        />
                                        <span class="h2 fw-bold mb-0">
                                            Welcome to <b>Desphixs👋</b>
                                        </span>
                                    </div>
                                    <h5
                                        class="fw-normal mb-3 pb-3"
                                        style={{ letterSpacing: 1 }}
                                    >
                                    </h5>
                                    <div class="form-outline mb-4">
                                        <input
                                            type="email"
                                            id="form2Example17"
                                            class="form-control form-control-lg"
                                            placeholder="Email Address"
                                            name="email"
                                            value="user@mail.com"

                                        />
                                        {#if errors.email }
                                            <p class="bg-red-100 border border-red-400 text-red-700 px-4 py-1 mt-1 rounded relative" role="alert">
                                                {@html errors.email }
                                            </p>
                                        {/if}
                                    </div>
                                    <div class="form-outline mb-4">
                                        <input
                                            type="text"
                                            id="form2Example17"
                                            class="form-control form-control-lg"
                                            placeholder="Username"
                                            name="username"
                                            value="user1"

                                        />
                                        {#if errors.username }
                                            <p class="bg-red-100 border border-red-400 text-red-700 px-4 py-1 mt-1 rounded relative" role="alert">
                                                {@html errors.username }
                                            </p>
                                        {/if}
                                    </div>
                                    <div class="form-outline mb-4">
                                        <input
                                            type="password"
                                            id="form2Example17"
                                            class="form-control form-control-lg"
                                            placeholder="Password"
                                            name="password"
                                            value="oasdjlaks12q3"
                                        />
                                        {#if errors.password }
                                            <p class="bg-red-100 border border-red-400 text-red-700 px-4 py-1 mt-1 rounded relative" role="alert">
                                                {@html errors.password }
                                            </p>
                                        {/if}
                                    </div>
                                    <div class="form-outline mb-4">
                                        <input
                                            type="password"
                                            id="form2Example27"
                                            class="form-control form-control-lg"
                                            placeholder="Confirm Password"
                                            name="password2"
                                            value="oasdjlaks12q3"
                                        />
                                        {#if errors?.password2?.length ?? 0 > 0}
                                            <p class="bg-red-100 border border-red-400 text-red-700 px-4 py-1 mt-1 rounded relative" role="alert">
                                                {@html errors.password2 }
                                            </p>
                                        {/if}
                                    </div>
                                    <div class="pt-1 mb-4">
                                        <button
                                            class="btn btn-white border btn-lg btn-block"
                                            type="submit"
                                        >
                                            Register
                                        </button>
                                    </div>
                                    <a class="small text-muted" href="#!">
                                        Forgot password?
                                    </a>
                                    <p class="mb-5 pb-lg-2" style={{ color: "#393f81" }}>
                                        Already have an account?{" "}
                                        <a href="/login" style={{ color: "#393f81" }}>Login Now</a>
                                    </p>
                                    <a href="#!" class="small text-muted">
                                        Terms of use.
                                    </a>
                                    <a href="#!" class="small text-muted">
                                        Privacy policy
                                    </a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>